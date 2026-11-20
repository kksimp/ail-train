# E14 pilot: why AIL lost on the held-out task

Date: 2026-11-16. Tree: main 1318e987. Source: `e14-e14-pilot-results.tgz`, the four
`invjson` AIL transcripts and their `.bench/runs.jsonl`, plus the two C transcripts.
Analysis only; nothing was run or built.

## Short answer

- The pilot ran **one** held-out task (`invjson`), two trials per arm. `calc` and `maze` were not in it.
- The loss is **not about the task being unseen**. `invjson` is the only one of the nine pilot tasks that
  prints literal `{` and `}` (JSON). All four AIL trials of it have `\{` in their final source; no other
  AIL trial in the pilot does.
- All 7 failed AIL versions are compile errors. None is a logic error, and every trial passed 22 of 22
  hidden cases once it built. 5 of the 7 come from literal braces in strings or the follow-on `\}` mistake.
- Three cheap compiler fixes (auto-fix only, no language change) would have removed 6 of the 7 failed
  versions: ail-plain 2.0 to 1.0, ail-core-card 3.5 to 1.5, against 1.5 for C.

## Every failed version

| trial | version | error | what the agent wrote | carried over from | what should have caught it |
|---|---|---|---|---|---|
| ail-plain-1 | v1 | `trait.op.1` `+` doesn't join strings | `"\\u00" + k.to_hex().pad_left(2, '0')` (added by a `sed` patch after the main write) | nearly every language | Auto-fix. The fix is already marked certain, but the rewriter gave up, so no `fix:` line and no rewrite (see fix 3) |
| ail-plain-2 | v1 | `lex.str.2` x2, `{` never closed | `"{"` and `"    {\"sku\": ..."` | every language where `{` in a plain string is text | Auto-fix. The `fix:` line was correct, but string-escape fixes are left out of the certain set on purpose (`compiler/fix/sure.ail`) |
| ail-core-card-1 | v1 | `lex.str.2` x2 | same two strings | same | same |
| ail-core-card-1 | v2 | `lex.str.1` x2, unknown escape `\}` | hand-fixed v1 and escaped the closing braces too | over-generalised from `\{`; not from another language | Auto-fix (`\}` to `}` has one meaning), or never reached if v1 is auto-fixed |
| ail-core-card-1 | v3 | `expr.name.1` `str` has no method `join` | `", ".join([...])` | Python | Auto-fix (`sep.join(xs)` to `xs.join(sep)`); it had help but no `fix:`. It was also in the file since v1 and stayed hidden behind the string errors for two rounds |
| ail-core-card-2 | v1 | `lex.str.2` x2, plus `type.coll.2` | the same two strings, plus `[""{t}"" for ...]` (dropped backslashes before the quotes) | braces as above; the quote slip is a plain typo, not a carry-over | Braces: auto-fix. Quote slip: nothing cheap; this version fails either way |
| ail-core-card-2 | v2 | `lex.str.1` x2, `\}` | hand-fixed v1 and escaped the closing braces too | as core-card-1 v2 | as core-card-1 v2. The agent then ran `ail fix`, which fixed it |

Things that went right: `const X = ...` was auto-fixed three times in core-card-2 (`mod.const.1`), format
specs (`{n:02x}`, `{h:0>2}`) and `else` on `to_int()` were right first time, and both arms found
`char.code()` and `int.to_hex()` with `ail ask`.

For comparison, C failed one version of two trials, on a logic bug (a missing string terminator after
reading a line, 1 of 5 visible cases passing), fixed in one round.

## Did the card cover it?

- Brace escape: both cards mention `\{` only as a trailing comment on an interpolation example
  (core card line 46, full card line 216); the full card adds "No `{{`: write `\{`" (line 235). Neither
  shows a string whose braces are all text, and neither says `}` is never escaped. One of two full-card
  trials got it right; neither core-card trial did.
- `+` on strings: both cards say it. The agent's main write obeyed it; the slip came in a later patch.
- `sep.join(xs)`: the core card shows `xs.join(", ")` but not the wrong form. The checker knows it
  (`compiler/check/foreign.ail`, `str.join`) and only prints help.

## Recommended fixes, ranked by failed versions removed (of 7)

1. **Auto-fix a literal `{` in a string when it is certain. Removes 4** (plain-2 v1, core-1 v1 and v2,
   core-2 v2; the two `\}` versions go because the agent never hand-escapes).
   Certain cases: the unclosed `{` is followed by `\"`, by the end of the string, or by a space or `\n`
   escape. Inside an interpolation a string literal is written with a plain `"`, so `{\"` can't start an
   expression. All six pilot instances are one of these. A `{` followed by a name with no `}` (a forgotten
   closer) stays a plain error. Needs a short ADR amending ADR 1130, which left string-escape rules out
   (an AI-delegated ADR, so no escalation). Place: `compiler/syntax/lex.ail` near line 1271, and the
   certainty mark.
2. **Auto-fix `\}` to `}`. Removes 2 alone** (core-1 v2, core-2 v2), 0 more after fix 1, but it is the
   safety net whenever an agent hand-escapes. Also add to the `lex.str.2` help: "`}` is never escaped".
3. **Make the `+` rewrite handle a char literal or an escape inside brackets. Removes 1** (plain-1 v1).
   `skip_brackets` in `compiler/fix/rewrite.ail` returns `none` on any `'`, so `"x" + s.pad_left(2, '0')`,
   the padding form the card itself teaches, gets no fix. `atom_before` has the same limit.
4. **Certain fix for `sep.join(xs)`. Removes 1** (core-1 v3). Receiver is `str`, one argument that is a
   list: rewrite to `xs.join(sep)`.
5. **Card, both versions (prevention; cheap, effect not measured here).** One line in the "not AIL" list
   or the traps section: `print("\{\"id\": {n}}")` with the note that every literal `{` in any string is
   `\{`, and `}` is never escaped. Add `", ".join(xs)` to the core card's list of rewritten spellings
   once fix 4 lands.
6. **Keep checking after a string error. Removes 0 once 1 to 4 land,** but it is the general form of the
   core-1 problem: the `join` error sat hidden for two rounds. `lex.str.2` and `lex.str.1` can recover by
   keeping the character as text, so the checker's errors in the same function still show (extends
   ADR 1136).
7. Minor: `type.coll.2` on `[""{t}""]` says "give every element the same type". Two string literals side
   by side should say a `"` inside a string is `\"`.

With 1, 3 and 4 the only failed version left is the quote typo: ail-plain 1.0 and 1.0, ail-core-card 1.0
and 2.0. That is 6 of 7 removed.

No language change is proposed. Accepting `\}` as an escape would also remove the two `\}` versions, but
it changes the language and adds a second spelling, so the auto-fix is the better tool.

## Noise or pattern?

- **The size of the gap is noise.** n=2 per arm on one task; C's 1.5 is one logic bug in two trials. The
  ail-plain interval against C includes zero.
- **The cause is a real pattern.** 3 of 4 AIL trials wrote a bare `{` in a string on their first version
  and both hand fixes in the core arm over-escaped `}`. Any task that prints JSON, C-like text or
  templates will hit it at about that rate until fix 1 lands. It is specific to literal braces, not to
  unseen tasks: on the other eight tasks AIL tied C.
- **Core card worse than full card (3.5 against 2.0) is not established.** The difference is the `\}`
  follow-on in both core trials and one Python `join`; with two trials each that can be chance. The full
  card's extra "No `{{`" sentence may help a little.
- For the full run: without fix 1, expect `invjson` to cost AIL about one extra version per trial. `calc`
  and `maze` have not been run at all, so there is no held-out evidence beyond brace-printing yet.

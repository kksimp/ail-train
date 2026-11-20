# Agent fluency: what still makes a first AIL draft fail, and what to change for 0.2

2026-11-15. Analysis only: nothing was built, no model was called, no money was spent, the repository was not
changed. Asked by the designer: 0.2 must lift AIL against C on iterations to working code, without compromising
the language design.

## Evidence

- Every `./build` and `./test` log of the 511 E13 trials (release asset on tag `agentbench-e13`): each distinct
  failed version of `src/`, with its error rules and the source line of each. 223 failed compiles in the three AIL arms.
- The S17 replay of 307 first drafts on the 0.2 compiler (`s17-out-20261115T205802-8102.txt`, `s17-show.txt`).
- The card as it stands in #1310 (7a593d99), `ITERATIONS.md`, `VERDICT.md`, `S17-fixes.md`.
- Limits: the drafts were written from the E13 cards. Whether the 0.2 card prevents a slip is a judgment, not a
  measurement. Counts are small (12 trials a cell), so treat the per-trial figures as plus or minus 0.1.

## The result in one table

Failed compiles per trial, `ail-plain`. E13 measured; the other rows replay the E13 failures with causes removed.
A version counts as saved only when every error in it is removed, so these are upper bounds.

| | New code (39 trials) | Change tasks (64 trials) |
|---|--:|--:|
| E13 measured | 0.69 | 0.45 |
| 0.2 as merged (batches c to f, #1310) | about 0.51 | about 0.36 |
| plus the three lanes in flight (`T ! str`, `x = e else` block, bare `eprint`) | about 0.33 | about 0.34 |
| plus items 1 to 5 below | about 0.18 | about 0.11 |
| C in E13 | 0.03 | 0.14 |

Two readings. On change tasks one item (public fields, item 1) is nearly the whole remaining gap, and with it AIL
is level with or ahead of C. On new code the in-flight lanes are the largest step, items 2 to 5 take the next
half, and what is left is single slips (a guessed method name, a missing `mut`) that only the card can prevent.

## A rule that changes how to rank fixes

Under the iteration metric a better diagnostic or an `ail fix` line saves nothing on the first failure: the
version was already handed in. It only prevents a second failure. In the plain arm 12 of 56 failed compiles were
second or later failures. So:

- A first failure is removed only by the language accepting the natural form, or by the agent not writing it
  (card, or what it already knows).
- Diagnostics matter for the 21% that are repeat failures, and for cost.
- `ail fix` was run in 3 of 307 AIL trials. Agents edit by hand from the printed `fix: write` line. Work on
  `ail fix` itself does not move this benchmark.
- Errors travel together: 3 of the 6 bare `eprint` drafts also call bare `exit`, and 2 of the 4 `T ! str` drafts
  also hold the result in a variable. A lane that fixes one of a pair saves no iteration on that draft.

## Ranked findings (not already in flight)

Saved iterations are per trial on the plain arm, from E13 frequencies, after the merged and in-flight work.

### 1. Fields of a `pub struct` are private unless each is marked. Language. Designer's decision (ADR 0098).

**Decided 2026-11-15 23:07Z by the designer: option (a), public by default.** Needs a new ADR superseding the field part of ADR 0098, a marker word for a private field (token measurement), spec `mod.vis.1` and `mod.vis.3`, the card's Modules example, and `compiler/check/privacy.ail`.

- stock-refactor, first draft: 10 of 13 plain, 6 of 13 tools and 9 of 13 core-card trials fail on `mod.vis.1`.
  The agent moves a struct into a module, marks the struct `pub`, and leaves the fields.
- 4 of the plain trials then fail a second time putting `pub` in the wrong place (`pub qty := number(...)` on a
  local, from a search and replace).
- It is not ignorance of the rule. Rust has the same rule, its agents know it, and they do worse on this task:
  2.25 failed compiles a trial against AIL's 1.42 and C's 0.75, with 84 "field is private" errors. C has no
  field privacy and is the arm that wins. A card line will not fix what Rust agents get wrong in Rust.
- This is 15 of the 29 failed compiles in the plain arm's whole change group.
- Options:
  a. Recommended: a field of a `pub struct` is public; a private field is marked (the marker word needs a token
     measurement). A private struct's fields stay module-private as now. Reading the declaration still tells
     the whole story, so local reasoning is kept, and the rare case (a type guarding an invariant) is the
     marked one. Existing code keeps compiling; some fields become visible that were not.
  b. Keep the rule; make `mod.vis.1` carry a cross-file fix. Saves the second failure only (about 0.06).
  c. Keep the rule and rely on the card's Modules example (already there in #1310). Rust's result says no.
- Estimate for (a): change tasks 0.34 to about 0.12; stock-refactor 1.4 to about 0.3; the same on till-rename.
  Nothing on new code.

### 2. Bare `exit` must land with bare `eprint`. Language (prelude). Same lane as `eprint`.

- 3 of the 6 plain drafts that write `eprint(...)` write `exit(1)` on the next line (4 of 7 counting the replay).
  With `eprint` alone those drafts still fail.
- Form: `exit(code int) never` in the prelude beside `print` and `eprint`; `io.exit` stays. It is the same
  argument as `eprint`: the three things every command-line program does are bare.
- Estimate: 0.03 alone, but it is what makes the `eprint` lane deliver its full 0.15.

### 3. `else` may take an optional fallback, so `e else none` is legal. Language, a generalisation.

- 5 plain trials (3 new code, 2 change), 8 across arms, first error `type.opt.4`: `v := s.to_int() else none`,
  `(m.get(k) else none) != none`. The agent believes an optional has to pass through `else`.
- Today the fallback must be a `T`. Allowing a `T?` fallback, with the result a `T?`, is the "or else try this"
  chain other languages have (`a else b else 0`), and `else none` falls out as a legal no-op. Warn that it is
  redundant, with the fix that drops it. No special case is added.
- The card also never says how to test an optional without binding it. Add one line to "Absence and errors":
  `x == none` and `x != none` test an optional; `m.contains(k)` tests a key; there is no `is some`.
  (`x is some` was 2 plain and 2 tools change-task failures.)
- Estimate: about 0.03 to 0.05 on both groups.

### 4. A result that can fail cannot be held in a local. Language, small. (ADR 0122, AI-decided.)

- 4 failed versions in plain, 3 in tools, all on ledger, and in 2 of the 4 `T ! str` drafts:
  `r := parse_line(l)`, then `if tx := r` and `else err`. `err.use.1` rejects the first line, and three
  follow-on errors come with it.
- An optional can be held (`x := m.get(k)`) and a result cannot. Allowing `r := f()` for an immutable local
  that is later consumed by `if v := r`, `r else ...`, `r?` or `return r` removes the asymmetry. Using `r` as a
  `T`, or never consuming it, stays an error, so "every failure is handled" is kept.
- Cheaper alternative with no language change: a fix on `err.use.1` that folds the two lines into
  `if tx := parse_line(l)`. That saves only repeat failures.
- Estimate: 0.05 to 0.08 on new code, and it is needed for the `T ! str` lane to clear its drafts.

### 5. `mut m := {}` is typed as a list unless its first use is a plain `m[k] = v`. Checker.

- 2 of 12 plain stock trials and 5 core-card versions: `mut qty := {}` then `qty[k] = qty.get_or(k, 0) + q`,
  or `if not items.contains(sku)` first. The errors say "a list index must be `int`" about a map.
- The card promises "typed by first use". Infer the map from `get`, `get_or`, `contains`, `push(k, x)` and from
  an assignment whose right side reads the same map. No language change. Unchanged in the replay (3 to 3).
- Estimate: 0.03 to 0.05 on new code.

### 6. The card's own Heap and Deque lines omit `mut`. Card. Certain, one line each.

- Both plain "missing `mut`" failures on depgraph, and one in tools, are `h := Heap[str]()` then `h.push(x)`,
  which is what the card's Lists section shows: "`h := Heap[int]()` ... `h.push(x)`", and "`d := Deque[int]()`".
- Write `mut h := Heap[int]()` and `mut d := Deque[int]()`. Worth a pass over every inline example for the
  same slip, since the doc-snippet check only covers fenced blocks.
- Estimate: 0.05 on depgraph-like tasks.

### 7. `List.get(i) T?`. Std, small. Already S17's quick win 5, not done.

- `argv.get(1) else ""` is the natural safe read of an argument (1 plain, more in core card). Map and Deque
  have `get`; the collection vocabulary rule (ADR 1099) argues for the sibling. Today's help suggests
  `argv.skip(i).first()`.

### 8. A one-character string literal where a `char` is expected. Language, small, optional.

- `pad_left(2, "0")`: 8 failed versions across tools and core card, none in plain (the Habits block covers it).
- AIL already types an int literal as a float where a float is expected (type.num.10). The same rule for a
  one-character string literal is consistent. Only the literal, never a `str` value. Low priority while the
  full card is the headline arm.

### 9. Diagnostics that prevent a second failure. Checker, each small.

- `err.decl.2` follow-ons: after the `! str` error, 2 of 4 plain trials wrote the `error enum` or
  `error struct` wrongly (`Fields Fields`, `reason str "{reason}"`). The `T ! str` lane removes the cause. If
  that lane is cut down, the help must show a complete declaration with a message.
- Unqualified names after a module split (`Kind`, `Event`, `Store`, `number`): 2 plain, 9 tools, 27 core-card
  versions. Give `expr.name.1` a fix when exactly one imported module exports the name: "write `event.Kind`".
- `x is some` / `x is none`: a `lex.stmt.1` today; name the form and fix to `!= none` / `== none`.

### Looked at and not recommended

- `+` on strings (1 plain, 9 other): a designer decision already made; the Habits block covers it.
- `contains_key`, `has`, `insert`, `keys()` on a set (2 plain, 20 other): aliases would break the one-vocabulary
  rule. Fix lines exist; the Habits block covers them.
- `else if` (0 plain, 3 other), `mut x = e` (0 plain, 6 core): both have fixes; the card covers them.
- Narrowing after `if x == none` (about 9 versions, mostly core card: `q.unwrap()`, `int?` compared): a real
  model mismatch, but a large semantic change. Item 3 plus the card line takes the common cases. Revisit after E14.
- `m[k] else d` (1 plain, 12 other): indexing traps by design; `get` is on the card.

## Not language: one harness fact that costs every arm turns

`sed -i 's/...'` fails on macOS (BSD sed needs `-i ''`). 240 of 480 such calls in E13 failed: plain 61 of 112,
tools 44 of 99, core card 77 of 165, C 21 of 39, Rust 37 of 65. A failed `sed` leaves the source unchanged, so
it does not add an iteration, but the agent builds again, sees the same error, and spends two turns. AIL arms
hit it most because they have the most one-line fixes. Neutral fix for E14: a GNU-compatible `sed` first on
PATH for every arm, or one line in the common prompt naming the platform.

## What this means for the E14 odds

- Fix an issue and extend or refactor: with item 1, AIL's failed compiles fall to about C's. Chance of level or
  better on the change group rises from the 25 to 45% in `ITERATIONS.md` to roughly 55 to 65%. Without item 1,
  stock-refactor and till-rename stay losses.
- New code: about 0.33 after the in-flight lanes, about 0.2 with items 2 to 6, against C's 0.03. AIL does not
  beat C here on compiles; it can reach a near tie in total iterations only where C fails tests (stock: 0.5).
  The held-out tasks that ask for what C makes hard remain the route to a new-code win.
- The remaining new-code failures are one-off slips spread over many forms. No single further language change
  is worth more than about 0.05; they add up only together.

## Suggested order

1. Decide item 1 (designer). It is the largest and the only one that reverses a designer ADR.
2. Add bare `exit` to the `eprint` lane, and item 4 (or its fix) to the `T ! str` lane, so each lane clears
   its drafts.
3. Items 3 and 5 as two small lanes; items 6 and the `== none` line into the card PR.
4. Items 7 to 9 if lanes are free.
5. `sed` in the harness before the pilot.

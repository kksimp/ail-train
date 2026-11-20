# E14 calculator-only rerun: analysis

Date: 2026-11-18. Tree: main 0384e848 (slice D, ADR 1140, and the `mut` forwarding fix are in). 36 trials, $4.91.
Source: `e14-calc-rerun-results.tgz`. Analysis only; nothing built or run, no paid trial.

| arm | correct | versions, all trials | confirmation run | full run |
|---|--:|--:|--:|--:|
| ail-plain | 10/12 | 1.83 | 2.33 | 2.25 |
| ail-core-card | 8/12 | 2.25 | 2.50 | 2.08 |
| c | 11/12 | 1.08 | 1.17 | 1.08 |

## Short answers

- **The hidden case** behind five of the six wrong AIL programs is `overflow-min`: the task's spec says the smallest
  value `%` -1 is an `overflow` error, and AIL defines `MIN % -1` as 0. It is the same case as in the full run.
- **No compiler bug in generated code.** The `mut` forwarding bug did not recur. Three bugs in fixes and messages
  did show up (section 3); one of them makes a certain fix turn a working program into one that stops.
- **`Fail` works.** 8 final programs use `! Fail`; the certain fix fired in 6 trials and compiled where it was
  applied. No trial failed because of `Fail` itself. The no-result `! str` problem (about 11 failed versions in the
  confirmation run) is down to 3, all from two gaps in when the fix is given.
- **The gap to C is now mostly one thing: a parameter stored into without `mut`** (`env[name] = v`): 7 of the 25
  failed AIL versions, 5 of the plain arm's 10. It was 4 of 34 before; it is the top cause now that the others shrank.

## 1. The wrong programs

| trial | failed case | cause |
|---|---|---|
| core 2, 4, 5; plain 7 | overflow-min | `a.checked_rem(b) else return "overflow"` with no test for the smallest value and -1; none of the four looked `checked_rem` up |
| core 8 | overflow-min, keywords | looked it up, read "`MIN % -1` is `0`", and wrote `if b == -1` then `return 0`, against the task's spec |
| plain 9 | tab-cr | whitespace handling, language-neutral (C lost one trial to `keywords` the same way) |

Every trial that looked `checked_rem` up with `ail ask` got it right except core 8 (8 of 9). The four that used it
from habit, without looking, all got it wrong: the name promises what it does in other languages. The core card has
no line on it, so the core arm only learns the difference by asking.

Not a compiler bug: `MIN % -1` being 0 is the mathematically right remainder and is the documented rule
(expr.arith.5). It is a place where the task's spec was written around C's behaviour.

What would close it:
- Core card: add to the arithmetic line "`a % -1` is 0, so `checked_rem` never reports the smallest value `%` -1"
  (about 15 tokens). The full card already says it. Likely recovers 3 of the 5.
- `ail ask` wording: the line now reads "`int.checked_rem(b)` is always `some(0)`, never `none`", which says the
  method always gives 0. It should read "`checked_rem(-1)` is `some(0)`, never `none`: ...". Small.
- Changing `checked_rem` to give `none` there would match habit, but then `checked_rem` would report a failure
  that `%` itself never has. Not recommended; it would be Kaleb's call.

## 2. The 25 failed AIL versions, by cause (plain 10, core card 15)

| cause | versions | trials | fixable how |
|---|--:|---|---|
| Store into a parameter without `mut` (`own.param.1`) | 7 | plain 4, 5, 7, 8, 10; core 8, 10 | certain fix, see below |
| `str ! str` (`err.str.2`), with three follow-on errors each | 4 | plain 11; core 2, 6, 12 | message only; no certain fix exists |
| No-result `! str` where the `Fail` fix was withheld | 3 | plain 2; core 5, 10 | two gaps in the fix, section 3 |
| Guessed or misused std calls (`a.min()`, `index_of`, `trim_start(' ')`, `trim_start_spaces`, `some(' ')`) | 4 | plain 3, 12; core 4, 7, 9 | help already names the right call; one version each |
| Other languages' forms (`x if c else y`, `mut pos int` as a field, `match` on a `char?`, `"{u else \"\"}"`) | 3 | plain 12; core 4, 6, 11 | card or message |
| A certain fix that broke the program (`pass` became `todo`) | 1 | core 10 | bug, section 3 |
| Logic and tokenizer errors | 3 | plain 5; core 2, 11 | language-neutral |

**`own.param.1` in detail.** All seven are `fn run_line(line str, env Map[str, int]) RESULT` ending in
`env[name] = v`. The certain fix (add `mut` to the parameter and at each call) exists, but I had it limited to
functions with no result, to protect a function that changes its own copy and returns it. Every one of these seven
has a result (`str?`, `int ! str`, `str`), so none got the fix. A rule that covers them and stays safe: the fix is
certain when the parameter is not read again after the store (not later in the function, and the store is not in a
loop that reads it). A store nothing reads can only have been meant for the caller. That alone would have removed
7 of 25 failed versions: plain about 1.83 to 1.42, core about 2.25 to 2.08.

## 3. Bugs found in fixes and messages (none in generated code)

1. **A certain fix that makes a program stop.** `gram.foreign.1` rewrote a lone `pass` to `todo`, which stops the
   program when reached (core 10: four visible tests failed with "reached a `todo` hole", one version lost). `pass`
   means "do nothing". A certain fix must never add a stop: delete the line when the block has other statements,
   and otherwise give help only. This should be fixed before the tag.
2. **The `Fail` fix is withheld when a no-result function is called with `?` as the last line of a branch of another
   no-result function** (`else` / `self.primary()?`). That `?` is counted as using the `str` result, but the caller
   is itself being rewritten and uses nothing. Plain 2 and core 10: the first build fixed some functions and left
   others, costing a second version. Rule: a `?` in the tail of a function that is itself an `err.str.4` function
   is not a use. The follow-on `expr.if.4` in such a body should also go.
3. **The `Fail` fix is withheld when one `return` has a string inside an interpolation** (`return "unknown {u else ""}"`,
   core 5): the fix can't find the end of that text. It should take the end from the parsed expression.
4. **`err.str.2` cascades.** Each `?` in a `str ! str` function also reports `err.prop.1` "this function can't
   fail", with the fix line "write `fn run_line(...) str ! str ! str`". Four trials saw four errors where one was
   meant, and the printed fix is wrong. Suppress `err.prop.1` in a function that has `err.str.2`.
5. `lex.str.2` on `"unknown {u else \"\"}"` offers `\{`, which is not what was meant (the quotes inside an
   interpolation need no backslash). Help text only.

## 4. What remains after those

`str ! str` (4 versions) has no automatic repair, because a returned text could be the result or the error. The
message is now one line and each case cost exactly one version. Guessed std names cost about one version per
five trials and are spread over many names. C's own figure on this task is 1.08, so parity here needs nearly every
first draft to compile; with sections 1 to 3 fixed I estimate plain at about 1.3 and the core card at about 1.8.
These are estimates from this run's counts, not measurements.

## 5. Recommendation

- Fix before the tag: item 1 of section 3 (a certain fix must not add a stop).
- Fix next, in one lane: the `own.param.1` rule, items 2 to 4 of section 3, the core card line and the `ail ask`
  wording. All are checker, fixer or card changes; none touches generated code.
- No further calculator run is needed to tag. The task is spent; a later measurement of these fixes should use a
  new held-out task of the same kind (a parser with variables), which would also show whether the gains carry over.

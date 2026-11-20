# E14 confirmation run: why the calculator gap stayed

Date: 2026-11-17. Tree: main 1636ca45. 108 trials, $12.62. Source: `e14-confirm-results.tgz` (metrics, build and
test outputs, final sources, transcripts). Analysis only; nothing built or run, no paid trial.

## Short answers

- `ledger-fix` is fixed (every arm 1.00; it was 2.00 for the plain arm). `ledger` is level with C (plain 1.17, C 1.08).
- The calculator did not move (plain 2.25 to 2.33 versions, core 2.08 to 2.50; C 1.17). The cause is still
  `T ! str`: about 20 of the 34 failed AIL versions. The new messages are read and obeyed, but each sends the
  agent to another form that also fails, so the rounds are spent anyway.
- **A real compiler bug surfaced: a `mut` scalar parameter that a function only passes on loses its change.**
  It produces wrong programs silently. This must be fixed before any tag.
- The wrong programs: core card 5 of 12, all five call `checked_rem`; plain 2 of 12 (one a hand-written overflow
  test, one the leading-spaces trap). The card line worked for the plain arm (no plain trial used `checked_rem`).
  It never reached the core arm: `ail ask` still prints "`none` on overflow or a zero divisor".
- The calculator should not block the 0.2 tag as a score. The miscompile should.

## 1. The miscompile (found by the agent in calc ail-core-card 9)

```ail skip=known-bug
fn inc(mut p int) int ! str
    p += 1
    return 5

fn o1(mut p int) int ! str
    l := inc(mut p)?
    l

fn main() !
    mut p := 0
    o1(mut p)?
    print("o1 {p}")     # prints 0; must print 1. With `p += 0` added in o1 it prints 1.
```

Cause, from reading `compiler/mir/lower_cell.ail`: a `mut` parameter of `int`, `bool`, `char`, `float`, `str`, an
enum or an optional arrives as a one-word cell. The callee reads it once and writes each assignment back through
`assign_param`. After a call that passes the name on with `mut`, `Lower.cells_back` (line 75) does
`write_var(c.key, cur, back)`: it rebinds the local but never stores into the function's own incoming cell. So the
caller's caller sees the old value unless the function also assigns the parameter itself.

Fix (to verify on the Mac): `write_var(c.key, cur, self.assign_param(c.key, c.ty, back, c.pos))`, the form
`lower.ail` line 1343 uses for an ordinary assignment. `assign_param` returns the value unchanged for a name that is
not a `mut` parameter. Tests needed: the program above with and without `?`, with `bool`, `str` and an optional, a
`mut self` enum method that forwards, a three-deep chain, and a `for mut x in xs` body that passes `x` on.
The runner should also say whether v0.1.0 has it (I expect yes: the file is not new). A recursive-descent parser
with a `mut pos int` is the textbook way to hit it.

## 2. Calculator: failed versions by cause (both AIL arms, 24 trials, 34 failed versions)

| cause | versions | note |
|---|--:|---|
| `fn f() ! str` meant as "no result, fails with text" | about 11 | `err.str.4` fires, but often only on the second build: a body that ends in an `if` whose branches are statements reports `expr.if.4` first |
| `str ! str` (`err.str.2`), usually the next thing tried | about 6 | agents then move to `int ! str` with a dummy value |
| `error struct Bad "{msg}"` written without its field line | 3 | all core card: the card and the help say "(field `msg str`)" in prose, and agents copied only the code |
| A text result returned from `T ! str` treated as the failure | 1 | plain 12 printed its results as errors |
| `env[k] = v` on a parameter without `mut` (`own.param.1`) | 4 | fix is `mut` on the parameter and at the calls |
| The `mut` forwarding miscompile | 2 | section 1 |
| Logic or tokenizer errors | 4 | language-neutral |
| Other, one each | 3 | `const`, `?` on an optional, a char literal |

What worked: the `return` auto-fix (`err.str.1`) and the `_ :=` auto-fix (`err.else.4`) both fired and rewrote the
source, and no trial hit the old "expected `!`, found `str`".

Why it didn't help the score: the function agents want here, "returns nothing or a line of text, and can fail with
a message", has no direct form in 0.2. `! str` and `str ! str` are both errors, and the working forms (an error
type, or a dummy `int` result) each cost a rewrite of every parser function. A message can't make that one step.

## 3. What is cheap

| fix | removes | size |
|---|---|---|
| `cells_back` stores through the incoming cell | wrong programs; 2 versions here | 1 line + tests |
| `ail ask`/`ail explain` text for `checked_rem`: "`checked_rem(-1)` is always 0, never `none`" | 5 of 12 wrong core programs | tiny (the text comes from the spec's first sentence; reorder it) |
| `err.str.4` also fires when the body ends in an `if` or `match` whose branches give no value | 3 to 4 | small |
| Help and card show the error type as two lines of code, not a line plus prose | 3 | tiny |
| `own.param.1` on `p[k] = v` or `p.push(x)`: certain fix adds `mut` to the parameter (the call-site `mut` fix already exists) | 4 | small |

These take the calculator from about 2.4 to about 1.9. They do not close it.

## 4. The decision that would close it

0.2 needs a way to write a function with no result that fails with text. Options:

- **A. A standard text error type, no new syntax (recommended).** For example `fn f() ! Fail`,
  `return Fail("syntax")`, and `else e` prints the text. Then `err.str.4` can carry a certain fix that rewrites
  `! str` to `! Fail` and each `return TEXT` to `return Fail(TEXT)`, so what agents write today compiles after one
  automatic rewrite. `str ! str` gets the same help. Cost: one std type and a rule; the name needs choosing.
- **B. A new spelling for "no result ! str".** Direct, but it is new syntax and `! str` already means something.
- **C. Leave it.** The calculator stays about one version behind C on any task shaped like a parser.

## 5. Should the calculator block the tag?

No, as a score. It is spent as a held-out task, one of its cases asks for an overflow that AIL defines away
(`MIN % -1` is 0), and the other eleven task results stand. Tag after: the miscompile fix (gated on all three
hosts, since it is native codegen), the `ail ask` text, and the small fixes above. Decide option A, B or C
separately; if A, it can be 0.2 or 0.2.1.

No further paid run is needed to tag. A rerun of the calculator alone (36 trials, about $5) would only be worth it
after option A or B lands.

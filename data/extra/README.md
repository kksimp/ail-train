# data/extra: programs written for training

Programs written for this project, beside the raw inputs in `data/raw/` and the corpus in kksimp/ail.

## drills/

40 short programs (20 to 60 lines), each built around built-in methods and forms that the AIL corpus and examples
use fewer than five times, and around the mistakes the agent drafts made most (`data/raw/draft-error-lines.txt`):
guessed method names, unhandled optionals and failures, `if` and `else` used as values.

Each `drills/NAME/` follows the corpus layout: `NAME.ail` (a `##` header that states the task, `fn main()`, `@test`s),
`NAME.py` (a Python twin that prints the same output) and `NAME.out` (written by the twin).
They feed the `write`, `port` and `complete` families.

## batchNN/

The D11 growth to about 3,000 checked programs (PLAN.md section 2): batches of about 100 programs in the same
`NAME/{NAME.ail,NAME.py,NAME.out}` layout, each a small realistic task (a header comment states it) that mixes
everyday forms with less common built-ins. Each batch is checked on the Mac before the next one is written.

- `batch01/`: 100 programs. First Mac check of 40: 36 passed; the 4 failures were `char.from_code` used as a `char`
  (it is a `char?`) and a `{...}` set comprehension inside a string interpolation (lexed as `{{`). All 100 pass.
- `batch02/`: 100 programs. First check: 97 passed; the 3 failures were `par` used as a name (it is a keyword),
  `"${x}"` (not interpolation in AIL; a check error) and a `_` loop variable nested in another `_` loop. All 100 pass.
- `batch03/`: 100 programs, checked in steps of 50, 70 and 100. The 9 early failures were `+` on strings
  (AIL has no string `+`; use interpolation), `lower`/`upper` (they are `to_lower`/`to_upper`) and `top(n)` read as pairs
  (it returns keys). All 100 pass.
- `batch04/`: 100 programs, checked in steps of 30, 50, 70 and 100, with more traits, generics, operator impls and
  struct methods. The 4 failures were a struct named `Task` (a prelude type), an enum interpolated as its bare
  variant (AIL prints `Priority.Urgent`), a literal `{` in a string (write `\{`) and `parse_int` (it is `to_int`).
  All 100 pass.
- `batch05/`: 100 programs, checked in steps of 20, 40, 60, 80 and 100: traits, generic structs, `Ord` from
  fields, sets, error results and everyday simulations. The 1 failure was a `str ! str` function (AIL can't tell
  the result from the error; use `str ! Fail`). All 100 pass.
- `batch06/`: 100 programs, checked in steps of 40, 60 and 100: numeric methods (bisection, Simpson, least
  squares, Cramer), classic algorithms (KMP, LZW, Huffman, LCS, page replacement, round robin) and everyday tasks.
  The 5 failures were `_` bound twice in one function (2), `+` on strings, `move` as a name (a keyword) and a
  mean on a rounding edge. The same PR replaced 19 programs in batch04 and batch05 that repeated earlier topics.
  All 100 pass.
- `batch07/`: 100 programs, checked in steps of 20, 40, 50, 60, 80 and 100: finance and science formulas, sorting
  and data-structure traces (radix, shell, Fenwick, open addressing), traits, `impl Ord`, `match` and `Fail`
  results. The 6 failures were `char.from_code` without `else`, `else` inside an index (needs parentheses), a
  Python `:+` sign in a twin, an `impl` block without a trait (struct methods are `fn T.name`) and a local named
  `bytes` (a type). All 100 pass.

## Status

**Checked: 740 of 740 pass** (40 drills, 100 each in batch01 to batch07) with ail 3d0c5c913 (0.2.0 release candidate) on 2026-11-21 (`RESULTS.txt`). On the drills' first
run 34 passed; 6 were fixed (four AIL forms guessed wrong: `str ! str`, calling a `fn` field as a method,
`Grid.to_list().sum()` on rows, an `if :=` on a failing result with no `else`; two Python twins were wrong).
These were written in a cloud session, where AIL builds are not allowed.
`tools/check_extra/run.sh` checks all of them on the Mac and writes `RESULTS.txt` here. The builder keeps only
programs that pass (PLAN.md section 5), so an unchecked or failing program never reaches training.

Rules for adding a program: deterministic, no files outside `fs.make_temp_dir`, no clock, random numbers or network,
output independent of map order, distinct from every eval task (PLAN.md 5.3).

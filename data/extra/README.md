# data/extra: programs written for training

Programs written for this project, beside the raw inputs in `data/raw/` and the corpus in kksimp/ail.

## drills/

40 short programs (20 to 60 lines), each built around built-in methods and forms that the AIL corpus and examples
use fewer than five times, and around the mistakes the agent drafts made most (`data/raw/draft-error-lines.txt`):
guessed method names, unhandled optionals and failures, `if` and `else` used as values.

Each `drills/NAME/` follows the corpus layout: `NAME.ail` (a `##` header that states the task, `fn main()`, `@test`s),
`NAME.py` (a Python twin that prints the same output) and `NAME.out` (written by the twin).
They feed the `write`, `port` and `complete` families.

## Status

**Checked: 40 of 40 pass** with ail 3d0c5c913 (0.2.0 release candidate) on 2026-11-20 (`RESULTS.txt`). On the first
run 34 passed; 6 were fixed (four AIL forms guessed wrong: `str ! str`, calling a `fn` field as a method,
`Grid.to_list().sum()` on rows, an `if :=` on a failing result with no `else`; two Python twins were wrong).
These were written in a cloud session, where AIL builds are not allowed.
`tools/check_extra/run.sh` checks all of them on the Mac and writes `RESULTS.txt` here. The builder keeps only
programs that pass (PLAN.md section 5), so an unchecked or failing program never reaches training.

Rules for adding a program: deterministic, no files outside `fs.make_temp_dir`, no clock, random numbers or network,
output independent of map order, distinct from every eval task (PLAN.md 5.3).

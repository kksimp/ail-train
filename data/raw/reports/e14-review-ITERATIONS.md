# Iterations to green: E13 baseline and the E14 metric

2026-11-15, R1. Added after the designer redefined the win (22:54Z): beating C means the fewest iterations to
working code, for new code and for fixing an issue, not the fewest tokens. Recomputed from the `runs.jsonl` of all
480 E13 trials. No model calls.

## Metric

- **Iteration:** one distinct version of `src/` (by checksum) that the agent handed to the toolchain: `./build`,
  `./test`, or a compiler or checker call on a file under `src/`.
- **Iterations to green:** the count up to and including the first version that passes `./test`. 1 means the
  first version worked. **Failed iterations** is that count minus 1, split into failed compiles and failed tests.
- **Not counted:** the untouched seed (reproducing a bug is not an iteration); scratch probes on files outside
  `src/`; lookups. Probes and lookups are reported beside it, never added in.
- **Same instrument in every arm:** `cc` and `rustc` need the logging shim that `ail` has. Until then count only
  `./build` and `./test`, as below.
- **A trial counts only if it is correct on the hidden cases.** A wrong trial is a loss, reported separately.
- **Splits:** new code (ledger, depgraph, stock, held-out tasks); fix an issue (ledger-fix, stock-bugfix,
  till-bugfix); extend or refactor (the rest) as secondary.
- **AIL arm, named in advance: `ail-plain`.** Under this metric the core card is the worst AIL arm (below), so
  the earlier lean toward it as headline arm does not carry over. It was a cost argument.

## E13 baseline (only `./build` and `./test` counted, seed excluded)

| Group | Arm | Trials | First version green | Failed iterations per trial (compile + test) |
|---|---|--:|--:|--:|
| New code | ail-plain | 39 | 12 (31%) | 0.95 (0.69 + 0.26) |
| | ail-tools | 39 | 11 | 1.21 (0.62 + 0.59) |
| | ail-core-card | 37 | 1 | 2.49 (1.89 + 0.59) |
| | c | 39 | 31 (79%) | 0.21 (0.03 + 0.18) |
| | rust | 37 | 30 | 0.19 (0.00 + 0.19) |
| Change | ail-plain | 64 | 33 (52%) | 0.62 (0.47 + 0.16) |
| | c | 64 | 42 (66%) | 0.23 (0.14 + 0.09) |
| | rust | 64 | 41 | 0.61 (0.41 + 0.20) |

Per task, failed iterations per trial, ail-plain against c: ledger 1.21 / 0.07; depgraph 0.58 / 0.00; stock
1.00 / 0.54; ledger-fix 0.00 / 0.08; stock-bugfix 0.69 / 0.31; stock-decimal 0.38 / 0.00; stock-locations
0.62 / 0.08; stock-refactor 1.38 / 0.69. (C's stock-bugfix log is incomplete: 12 trials have no logged passing
`./test` on a changed version, so that cell is unreliable.)

Reading: AIL's test failures are about the same as C's. The whole difference is failed compiles. On new code C
fails to compile once in 39 trials.

## Estimate for 0.2

- New code: plain 0.4 to 0.6 failed iterations against C's 0.2. Chance plain is at or below C: about 10 to 15%.
  The S17 replay moved clean first drafts from 36% to 44% with the compiler alone; the card must do the rest.
- Fix an issue: already level in E13 on ledger-fix; chance of level or better about 40 to 50%.
- Extend or refactor: plain 0.35 to 0.5 against C's 0.2 to 0.3; about 25%. Level with Rust already.
- C cannot be beaten where it scores zero. On ledger, depgraph and stock-decimal the best AIL can do is tie.
  AIL can win only on tasks where C itself needs a second try: stock, stock-refactor, and tasks that demand
  what C makes hard.

## What most improves AIL's odds on this metric

1. Remove the remaining first-draft compile errors on ledger (1.0 a trial, the worst cell): `T ! str`,
   `x = e else` with a block, bare `eprint`. Under this metric each costs a whole iteration, so the pending
   language proposals matter more than they did for cost.
2. The module errors on stock-refactor (1.38 a trial): the fence-split fix and the card's Modules section.
3. The silent traps (`\r` in `lines()`, copies of map entries): each is a failed test iteration or a hidden failure.
4. Held-out tasks that state requirements C handles badly (input of any length, sums past 64 bits, nested
   data). These are where C will need iterations and AIL need not.
5. Card size no longer counts against AIL here, so the full card stays, and nothing should be cut from it for cost.

# ail-train results

What training does for a small model writing AIL, before and after, on the same test. The plan and the method are in
[PLAN.md](PLAN.md); this page holds the scores.

## Headline

| Model | pass@1 (all families) |
|---|---|
| ~1.5B base, no training | **11.5%** |
| ~1.5B, run 2 (Mac, MLX, rank 16) | **32.7%** |
| ~1.5B, PC run 1 (rank 64, sequence 4096) | **41.6%** |
| ~7B (PC, training) | *to come* |

Training took the small model from about one task in nine to about two in five, and the compile rate from 18% to 63%.

## The test

The quick eval: 218 items held out of training by program group (no program in the test appears in the training data,
and near-duplicates are dropped). Each item is sampled 3 times at temperature 0.2. An answer **passes** only when the
program it makes passes `ail check` and `ail run` prints exactly what the reference prints. pass@1 is the mean over the
samples, pass@3 counts an item when any sample passes. Every arm uses the same one-line system prompt and the same AIL
compiler (pinned in `.ail-version`). All scores are on the Mac with MLX at 4 bits.

| Family | Items | What the model gets | What it must produce |
|---|---|---|---|
| fixline | 32 | a program with one injected mistake and the line it is on | the corrected line |
| fix | 28 | a real agent draft that fails to compile, with the compiler's message | the whole fixed program |
| cursor | 32 | a program with a gap at the cursor (rest of a line, or 1 to 5 lines) | the missing text |
| complete | 31 | the start of a program | the rest of it |
| function | 31 | a program missing one function, with its signature | the function |
| port | 32 | a Python program | the same program in AIL |
| write | 32 | a task description | a whole AIL program |

The first five are the ail-edit use: autocompletion and error fixing. port and write are whole-program work.

## ~1.5B: before and after

pass@1 in percent (compile rate in brackets).

| Family | Base | Run 2 | PC run 1 | Change, base to PC run 1 |
|---|---|---|---|---|
| fixline | 0 (0) | 100 (100) | **100** (100) | +100 |
| fix | 73.8 (73.8) | 83.3 (86.9) | **91.7** (91.7) | +17.9 |
| cursor | 0 (0) | 25.0 (43.8) | **51.0** (77.1) | +51.0 |
| complete | 10.8 (30.1) | 12.9 (41.9) | **24.7** (71.0) | +13.9 |
| function | 3.2 (26.9) | 10.8 (62.4) | **20.4** (69.9) | +17.2 |
| port | 0 (0) | 2.1 (4.2) | **8.3** (21.9) | +8.3 |
| write | 0 (0) | 0 (2.1) | 0 (14.6) | 0 |
| **All** | **11.5** (17.6) | **32.7** (48.0) | **41.6** (63.1) | **+30.1** |
| pass@3, all | 13.3 | 33.9 | 44.0 | |
| Eval time | 67 min | 113 min | 66 min | |

What the table says:

- **Error fixing is solved at this size.** fixline went from 0 to 100 and fix from 74 to 92. The untrained model could
  not even return a single corrected line in the expected form.
- **Autocomplete went from nothing to usable.** cursor went from 0 to 51, and 77% of its answers now compile.
- **Small functions and completions doubled from run 2 to PC run 1** (function 10.8 to 20.4, complete 12.9 to 24.7).
- **Whole programs are the gap.** write is still 0 and port 8; the compile rate for write rose from 0 to 15%, so the
  model is learning the syntax but not yet whole working programs. This is the job of the ~7B model.

## The runs

| | Run 2 | PC run 1 |
|---|---|---|
| Date | 2026-11-22 | 2026-11-22 |
| Machine | Mac (8 GB), MLX | PC (CUDA), exported to the Mac |
| Base weights | 4-bit, adapter on top | bf16, adapter merged, then 4-bit for the eval |
| LoRA | rank 16, last 16 of 28 blocks | rank 64, every linear layer of all 28 blocks |
| Sequence cap | 3072 | 4096 |
| Learning rate | 5e-5, warmup 100 | 1e-4 |
| Batch | 1 x 8 accumulation | 2 x 8 accumulation |
| Training items | 15,680 (data build 3d9570a) | 15,739 (data build 68384df) |
| Length | 6,232 iterations, ~0.4 epoch | 1,800 steps, 1.83 epochs (stopped when validation rose twice); best checkpoint step 1400 |
| Validation loss | 0.518 (still falling) | 0.190 at step 1400 |
| Training time | about 4.4 hours, two restarts from checkpoints | 2.1 hours |

Run 1 (2026-11-22, an older 119-item eval) scored 30.3% against a 17.4% base; its numbers are in PLAN.md section 9 and
are not comparable to the 218-item table above.

## How good is this? A rough yardstick

Published numbers measure different tasks with different scoring, so these are for scale, not a head-to-head.

- **Python, the best case.** The same ~1.5B base's own report gives about 77% exact first-line match on Python
  fill-in-the-middle and about 44% (base) to 70% (instruct) on HumanEval. Python has more training data than any other
  language, so that is a ceiling. Our cursor score (51%) is in range on a stricter test (the whole program must compile
  and print the right output); function and complete (20 to 25%) are about a third to a half of the Python level.
- **Languages models barely know.** Fine-tuning a 1B code model on Racket, OCaml and Lua reached about 17% pass@1
  averaged over MultiPL-E, and that was the state of the art for those languages
  ([MultiPL-T](https://arxiv.org/abs/2308.09895)). AIL is newer than all three and had no public training data.
- **Real editors.** GitHub Copilot users keep about 27% to 33% of the suggestions they are shown
  ([Ziegler et al.](https://arxiv.org/abs/2205.06537), [ZoomInfo study](https://arxiv.org/abs/2501.13282)). A
  different measure, but it shows a useful autocomplete is far from 100%.

## ~7B

Training on the PC (PLAN.md D15). Its row goes in the headline and a before-and-after table like the one above once the
run ends and the quick eval has scored both the untrained and the trained model.

## Reproducing a row

```
ARM=A0 tools/eval_quick.sh                                    # base, one-line prompt
ARM=C tools/eval_quick.sh                                     # base + the newest Mac adapter
tools/import_mlx.sh FOLDER/merged-bf16                        # a PC model, then:
MODEL_DIR=~/ail-train-work/mlx/NAME-4bit ARM=M tools/eval_quick.sh
```

Each run writes `~/ail-train-work/runs/eval-ARM-STAMP/summary.json`. The rows above come from `eval-A0-20261122T122810Z`,
`eval-C-20261122T122800Z` and `eval-M-20261122T225433Z`.

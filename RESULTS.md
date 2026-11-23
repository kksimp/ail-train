# ail-train results

What training does for a small model writing AIL, before and after, on the same test. The plan and the method are in
[PLAN.md](PLAN.md); this page holds the scores.

## Headline

| Model | pass@1 (all families) |
|---|---|
| ~1.5B base, no training | **11.5%** |
| ~1.5B, run 2 (Mac, MLX, rank 16) | **32.7%** |
| ~1.5B, PC run 1 (rank 64, sequence 4096), 4-bit | **41.6%** |
| ~1.5B, PC run 1, 8-bit | **44.8%** |
| ~7B, PC run 1 (QLoRA rank 32, step 800), 4-bit | **51.7%** |

Training took the small model from about one task in nine to almost one in two, and the compile rate from 18% to 73%.
The ~7B reaches one in two at 4 bits and is the first model to port Python programs at a useful rate (33%).

These are the Mac reference numbers: every model is copied from the PC over the shared drive and scored on the Mac with
MLX, so all rows share one machine, one sampler and one compiler.

## The test

The quick eval: 218 items held out of training by program group (no program in the test appears in the training data,
and near-duplicates are dropped). Each item is sampled 3 times at temperature 0.2. An answer **passes** only when the
program it makes passes `ail check` and `ail run` prints exactly what the reference prints. pass@1 is the mean over the
samples, pass@3 counts an item when any sample passes. Every arm uses the same one-line system prompt and the same AIL
compiler (pinned in `.ail-version`). All scores are on the Mac with MLX, at 4 bits unless a row says 8-bit; a base and
its trained model are always compared at the same precision.

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

pass@1 in percent (compile rate in brackets). The first four columns are 4-bit. "PC best" is the best-validation
checkpoint (step 1400), "PC final" the weights where the overfitting guard stopped the run (step 1800).

| Family | Base | Run 2 | PC best | PC final | PC best, 8-bit | Change, base to PC best |
|---|---|---|---|---|---|---|
| fixline | 0 (0) | 100 (100) | **100** (100) | 100 (100) | **100** (100) | +100 |
| fix | 73.8 (73.8) | 83.3 (86.9) | **91.7** (91.7) | 90.5 (90.5) | **97.6** (97.6) | +17.9 |
| cursor | 0 (0) | 25.0 (43.8) | **51.0** (77.1) | 55.2 (84.4) | **59.4** (93.8) | +51.0 |
| complete | 10.8 (30.1) | 12.9 (41.9) | **24.7** (71.0) | 14.0 (68.8) | **25.8** (82.8) | +13.9 |
| function | 3.2 (26.9) | 10.8 (62.4) | **20.4** (69.9) | 17.2 (79.6) | **22.6** (83.9) | +17.2 |
| port | 0 (0) | 2.1 (4.2) | **8.3** (21.9) | 14.6 (31.2) | **13.5** (28.1) | +8.3 |
| write | 0 (0) | 0 (2.1) | 0 (14.6) | 0 (20.8) | 0 (28.1) | 0 |
| **All** | **11.5** (17.6) | **32.7** (48.0) | **41.6** (63.1) | **41.0** (67.4) | **44.8** (72.9) | **+30.1** |
| pass@3, all | 13.3 | 33.9 | 44.0 | 43.6 | 47.2 | |
| Eval time | 67 min | 113 min | 66 min | 63 min | 88 min | |

- **4 bits cost the small model about 3 points** (44.8 at 8-bit vs 41.6 at 4-bit), mostly in cursor and fix, and
  nearly 10 points of compile rate. The 8-bit model (1.5 GB) is the one to ship in ail-edit.
- **The best-validation checkpoint beats the final weights** (41.6 vs 41.0): final ports better but completes worse, so
  the overfitting guard kept the right checkpoint.

What the table says:

- **Error fixing is solved at this size.** fixline went from 0 to 100 and fix from 74 to 92. The untrained model could
  not even return a single corrected line in the expected form.
- **Autocomplete went from nothing to usable.** cursor went from 0 to 51, and 77% of its answers now compile.
- **Small functions and completions doubled from run 2 to PC run 1** (function 10.8 to 20.4, complete 12.9 to 24.7).
- **Whole programs are the gap.** write is still 0 and port 8; the compile rate for write rose from 0 to 15%, so the
  model is learning the syntax but not yet whole working programs. This is the job of the ~7B model.

## PC cross-check

The PC scores the same 218 items with a different stack (transformers + PEFT on CUDA, adapter unmerged; the ~7B base
loaded at 4 bits with bitsandbytes NF4). pass@1 in percent (compile rate in brackets).

| Family | ~1.5B base, bf16 | ~1.5B PC best, bf16 | ~1.5B PC final, bf16 | ~7B base, NF4 | ~7B step 800, NF4 | ~7B final, NF4 |
|---|---|---|---|---|---|---|
| fixline | 0 (0) | 100 (100) | 100 (100) | 0 (0) | 96.9 (96.9) | 96.9 (96.9) |
| fix | 38.1 (38.1) | 91.7 (91.7) | 96.4 (96.4) | 83.3 (86.9) | 84.5 (86.9) | 92.9 (92.9) |
| cursor | 0 (1.0) | 56.2 (92.7) | 56.2 (96.9) | 3.1 (4.2) | 70.8 (92.7) | 70.8 (96.9) |
| complete | 7.5 (12.9) | 20.4 (65.6) | 23.7 (76.3) | 12.9 (20.4) | 38.7 (74.2) | 43.0 (88.2) |
| function | 0 (11.8) | 23.7 (77.4) | 22.6 (79.6) | 9.7 (28.0) | 46.2 (92.5) | 43.0 (82.8) |
| port | 0 (0) | 11.5 (26.0) | 10.4 (31.2) | 0 (0) | 28.1 (36.5) | 34.4 (39.6) |
| write | 0 (0) | 0 (17.7) | 0 (26.0) | 0 (0) | 0 (18.8) | 0 (29.2) |
| **All** | **6.0** (8.6) | **42.7** (66.8) | **43.4** (71.9) | **14.4** (18.7) | **51.7** (70.8) | **53.8** (74.8) |
| pass@3, all | 9.6 | 45.9 | 44.5 | 15.1 | 54.1 | 56.9 |
| Eval time | 62 min | 129 min | 122 min | 75 min | 148 min | 122 min |

- **The trained ~1.5B agrees across machines** (42.7 PC bf16 against 41.6 Mac 4-bit and 44.8 Mac 8-bit).
- **Untrained bases are setup-sensitive**: the ~1.5B base scores 6.0 on the PC and 11.5 on the Mac. Compare a base with
  its trained model on the same machine only.
- **The ~7B step 800 scores 51.7 on both machines** (PC: NF4 base + adapter; Mac: merged, 4-bit MLX), up from 14.4
  untrained: training adds about 37 points.
- **The ~7B final weights (step 1968) beat step 800 on the PC**, 53.8 against 51.7, mostly in fix (+8.4), complete
  (+4.3) and port (+6.3), although their validation loss was higher (0.144 against 0.139). The Mac score of the final
  weights goes in the ~7B section when it is in.

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

The ~7B (PC run 1, 2026-11-22): QLoRA on a 4-bit base, rank 32 on every linear layer, sequence 4096, batch 1 x 16
accumulation, learning rate 1e-4, the same 15,739 items, 2 epochs (1,968 steps, 8.4 hours, peak 6.6 GB of GPU memory).
Validation 0.175, 0.155, 0.145, **0.139** at step 800 (end of the first epoch), then 0.143 to 0.146 for the second.
As with the ~1.5B, one epoch of this data is enough.

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

## ~7B: the whole-program model

pass@1 in percent (compile rate in brackets), 4-bit. The ~7B was trained on the PC (PLAN.md D15) with QLoRA; this is its
best-validation checkpoint, step 800 of 1,968 (val 0.139; the second epoch did not improve it). The untrained ~7B and the
final weights are scored on the PC, which decides whether the final weights are worth a Mac run.

| Family | ~1.5B PC best, 4-bit | ~1.5B PC best, 8-bit | ~7B step 800, 4-bit |
|---|---|---|---|
| fixline | 100 (100) | 100 (100) | 96.9 (96.9) |
| fix | 91.7 (91.7) | 97.6 (97.6) | 94.0 (95.2) |
| cursor | 51.0 (77.1) | 59.4 (93.8) | **64.6** (87.5) |
| complete | 24.7 (71.0) | 25.8 (82.8) | **36.6** (79.6) |
| function | 20.4 (69.9) | 22.6 (83.9) | **40.9** (94.6) |
| port | 8.3 (21.9) | 13.5 (28.1) | **33.3** (44.8) |
| write | 0 (14.6) | 0 (28.1) | 0 (27.1) |
| **All** | 41.6 (63.1) | 44.8 (72.9) | **51.7** (74.6) |
| pass@3, all | 44.0 | 47.2 | 56.4 |
| Eval time | 66 min | 88 min | 215 min |

- **The ~7B doubles function writing** (41 vs 20 to 23) and **quadruples porting** (33 vs 8 to 14), the whole-program
  work it was trained for. It is also the best autocomplete (cursor 65).
- **Error fixing is a tie**: the small model at 8-bit already fixes as well or better.
- **write is still 0 for every model.** Compile rates of 15 to 28% show the models produce valid AIL, but not yet a whole
  program that prints exactly the right output.
- On the Mac the ~7B (4.3 GB at 4 bits) runs about 3x slower than the ~1.5B, fine for on-request work but slow for
  as-you-type completion.

## Reproducing a row

```
ARM=A0 tools/eval_quick.sh                                    # base, one-line prompt
ARM=C tools/eval_quick.sh                                     # base + the newest Mac adapter
MODEL_DIR=/Volumes/ailshare/ail-train/RUN/mlx-4bit ARM=M tools/eval_quick.sh   # a PC model, read from the share
```

The PC writes each model to the shared drive as `ail-train/RUN/` with `merged-bf16/`, `mlx-4bit/` (and `mlx-8bit/` for
the ~1.5B) and `SHA256SUMS.txt`; check with `shasum -a 256 -c SHA256SUMS.txt`, then point `MODEL_DIR` at the MLX folder.
Reading the model straight from the share keeps the Mac's disk free. To convert a `merged-bf16/` on the Mac, use
`tools/import_mlx.sh` on a local copy: run against the share directly, the GPU convert hit a Metal timeout.

Each run writes `~/ail-train-work/runs/eval-ARM-STAMP/summary.json`. The rows above come from:

| Row | Run folder |
|---|---|
| ~1.5B base | `eval-A0-20261122T122810Z` |
| ~1.5B run 2 | `eval-C-20261122T122800Z` |
| ~1.5B PC best, 4-bit | `eval-M-20261122T225433Z` |
| ~1.5B PC best, 8-bit | `eval-M-20261123T074559Z` |
| ~1.5B PC final, 4-bit | `eval-M-20261123T091553Z` |
| ~7B step 800, 4-bit | `eval-M-20261123T101920Z` |

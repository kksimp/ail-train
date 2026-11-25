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
| ~7B, PC run 1, final weights (step 1968), 4-bit | **52.4%** |
| ~7B, PC run 3, final weights (step 1488), 4-bit | *Mac reference pending* |

Training took the small model from about one task in nine to almost one in two, and the compile rate from 18% to 73%.
The ~7B reaches one in two at 4 bits and is the first model to port Python programs at a useful rate (33%). Given up
to 3 rounds of `ail check` feedback it rises from 53.8% to 56.4% (PC), with whole programs still at 0
([arm B](#7b-with-compiler-feedback-arm-b)).

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
  (+4.3) and port (+6.3), with function down 3.2, although their validation loss was higher (0.144 against 0.139). The Mac score of the final
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
best-validation checkpoint, step 800 of 1,968 (val 0.139), and the final weights at step 1,968 (val 0.144). The untrained
~7B is scored on the PC only (14.4%, see the PC cross-check).

| Family | ~1.5B PC best, 4-bit | ~1.5B PC best, 8-bit | ~7B step 800, 4-bit | ~7B final, 4-bit |
|---|---|---|---|---|
| fixline | 100 (100) | 100 (100) | 96.9 (96.9) | 96.9 (96.9) |
| fix | 91.7 (91.7) | 97.6 (97.6) | 94.0 (95.2) | 92.9 (92.9) |
| cursor | 51.0 (77.1) | 59.4 (93.8) | **64.6** (87.5) | 63.5 (91.7) |
| complete | 24.7 (71.0) | 25.8 (82.8) | **36.6** (79.6) | **40.9** (86.0) |
| function | 20.4 (69.9) | 22.6 (83.9) | **40.9** (94.6) | 38.7 (87.1) |
| port | 8.3 (21.9) | 13.5 (28.1) | **33.3** (44.8) | **38.5** (43.8) |
| write | 0 (14.6) | 0 (28.1) | 0 (27.1) | 0 (41.7) |
| **All** | 41.6 (63.1) | 44.8 (72.9) | **51.7** (74.6) | **52.4** (76.8) |
| pass@3, all | 44.0 | 47.2 | 56.4 | 56.9 |
| Eval time | 66 min | 88 min | 215 min | 222 min |

- **The ~7B doubles function writing** (41 vs 20 to 23) and **quadruples porting** (33 vs 8 to 14), the whole-program
  work it was trained for. It is also the best autocomplete (cursor 65).
- **Final weights vs step 800 on the Mac: 52.4 vs 51.7**, close to the PC's gap (53.8 vs 51.7). The final weights
  complete and port better (+4.3, +5.2) and fix a little worse; function and cursor dip by about 1 to 2 points. Despite
  the higher validation loss, the final weights are the ~7B to use.
- **Error fixing is a tie**: the small model at 8-bit already fixes as well or better.
- **write is still 0 for every model.** Compile rates of 15 to 28% show the models produce valid AIL, but not yet a whole
  program that prints exactly the right output.
- On the Mac the ~7B (4.3 GB at 4 bits) runs about 3x slower than the ~1.5B, fine for on-request work but slow for
  as-you-type completion.

## ~7B with compiler feedback (arm B)

Everything above is one shot: the model answers once and is scored. Arm B (2026-11-24) asks whether AIL's compiler
can steer the model to a working program. Same ~7B final weights (PC, NF4), same 218 items, prompt, seeds, 3 samples at
temperature 0.2 and the same pass rule. The only change: a sample whose program fails `ail check` gets up to 3
correction rounds. Each round sees the task, its current complete program, the exact `ail check` output and the
number of rounds left, and answers with a whole program. It never sees the expected output, the reference, a test or
any documentation, and it has no other tool. A program that passes `ail check` gets no more rounds, even if it then
fails at run time. Round 0 is arm A rerun in the same process (53.8%, as in the PC cross-check), so the arms are
paired. Script: `tools/eval_loop.py` (`tools\pc\run.ps1 evalloop big`, `ADAPTER=final`).

| Family | Compile, A → B | pass@1, A → B | pass@3, A → B | Failed compiles: compile / pass in the end | Error recurrence | Tokens per sample, A → B | Seconds per sample, A → B |
|---|---|---|---|---|---|---|---|
| fixline | 96.9 → 100 | 96.9 → **100** | 96.9 → 100 | 100 / 100 | 57.1 | 1,099 → 1,543 | 1.7 → 11.9 |
| fix | 92.9 → 98.8 | 92.9 → **96.4** | 92.9 → 96.4 | 83.3 / 50.0 | 25.0 | 236 → 310 | 1.6 → 2.7 |
| cursor | 96.9 → 96.9 | 70.8 → 70.8 | 71.9 → 71.9 | 0 / 0 | 66.7 | 995 → 1,102 | 1.4 → 1.8 |
| complete | 88.2 → 96.8 | 43.0 → 44.1 | 48.4 → 48.4 | 72.7 / 9.1 | 29.2 | 998 → 1,645 | 3.5 → 19.7 |
| function | 82.8 → 94.6 | 43.0 → **46.2** | 51.6 → 58.1 | 68.8 / 18.8 | 56.2 | 1,038 → 2,060 | 5.2 → 35.6 |
| port | 39.6 → 55.2 | 34.4 → **41.7** | 40.6 → 53.1 | 25.9 / 12.1 | 81.2 | 1,516 → 6,154 | 28.6 → 169.0 |
| write | 29.2 → 52.1 | 0 → 0 | 0 → 0 | 32.4 / 0 | 81.5 | 829 → 4,667 | 26.4 → 157.6 |
| **All** | **74.8 → 84.6** | **53.8 → 56.4** | **56.9 → 60.6** | 38.8 / 10.3 | 74.4 | 971 → 2,543 | 10.0 → 58.2 |

Compile and pass in percent of samples (pass@3 of items). "Failed compiles": of the samples whose first program failed
`ail check` (165 of 654), the share that compiled after the rounds and the share that printed the right output. Error
recurrence: correction rounds whose program still fails with a diagnostic rule ID the round before also had.

- **Compiler feedback adds 2.6 points overall** (53.8 to 56.4) and 10 points of compile rate, at 2.6x the tokens and
  5.8x the time per sample. Against the thresholds Kaleb set before the run (final exact output 0-5%: feedback alone
  is not enough; 10-20%: meaningful recovery), whole programs land in the first band (write 0%), and of the samples
  that failed to compile at first 10.3% end correct, the low edge of meaningful.
- **Port gains the most**: pass@1 34.4 to 41.7 and pass@3 40.6 to 53.1.
- **write stays at 0.** Its compile rate rises from 29 to 52%, but none of the 50 compiling programs prints the right
  output (11 of them fail at run time). The missing piece for whole programs is behaviour, not syntax.
- **Wins come early or not at all.** Of 369 passing samples, 352 pass at round 0 and 9, 3 and 5 in rounds 1 to 3, so it
  does not get lucky on the third try; it converges in one round or stays stuck.
- **Stuck samples repeat themselves.** Of the 44 write samples still failing after 3 rounds, 41 kept one rule ID in all
  four revisions, 18 kept the same set and 8 resubmitted an identical program every time (port: 35 and 15 of 43). 45% of
  all correction rounds returned an unchanged program. The most common write diagnostics: `expr.name.1` (unknown
  name, 75 revisions), `type.coll.2` (43), `trait.op.3` (27), `std.use.2` (23), `expr.call.2` (21).

What it means: the compiler loop works as a repair channel for surface errors (names, collection types, imports), and
the trained model reads the diagnostics. It does not yet make a 7B write a whole correct program. That needs
whole-program training data and probably training on correction transcripts like these, so the model learns to change
its program when a diagnostic repeats. This compares AIL with and without its own feedback loop; it says nothing about
AIL against another language.

Run: PC, 2026-11-24 03:26 to 14:07 UTC (641 minutes). Every revision is saved on the share in
`ail-train/pc-evals/7b-final-bnb4-armB/` (`revisions.jsonl`, `summary.json`, `console.log`).

## ~7B run 3: whole-program correctness

Run 3 (PC, 2026-11-25) retrains the ~7B from a fresh adapter on data aimed at whole programs that work, not only
compile: input-driven tasks, programs from real AIL applications, minimal repairs of the model's own failed drafts and
behaviour fixes. It is scored against the run 1 final weights (the baseline below) on a new, faster eval path and on a
new held-out set, dev-task.

### Data (build v3, ail-train 9ee30aa)

23,807 training items, 22.34M tokens (cap 26M), sequence cap 4,096.

| Family | Items | Tokens | What it is |
|---|---|---|---|
| appfn | 2,648 | 4.23M | a function from a real AIL application, its file as context |
| repair | 2,061 | 3.33M | a program that fails `ail check`, its diagnostics, the minimal fix (36 from the model's own harvested failures) |
| port | 2,759 | 2.43M | Python to AIL |
| behave | 1,595 | 2.23M | a program that compiles but prints the wrong thing, the fix (95 harvested) |
| spec | 2,800 | 2.04M | a task with its exact expected output, the program |
| fixline | 2,797 | 1.90M | as in the quick eval |
| cursor | 2,802 | 1.56M | as in the quick eval |
| complete | 2,111 | 1.24M | as in the quick eval |
| function | 1,853 | 1.12M | as in the quick eval |
| write | 779 | 0.70M | as in the quick eval |
| testfn | 700 | 0.47M | a function from its tests |
| appfile | 220 | 0.41M | a whole application file |
| task | 263 | 0.27M | an input-driven program: a full spec and two example cases |
| fix | 269 | 0.21M | as in the quick eval |
| change | 63 | 0.17M | an edit to a program, described in words |
| explain | 87 | 0.02M | what a program does |

- **Guards** (all passed): the build is deterministic (built twice, byte-identical); `quick-eval.jsonl` and
  `valid.jsonl` match `data/splits.sha256`; train items sharing more than 30% of token 8-grams with a quick-eval or
  dev-spec program are dropped (21 dropped); every `task` program passed `ail check` and printed each case's expected
  output (263 of 263). Held-out hashes (`data/splits.sha256`): quick-eval `2c080093…`, valid `d6f13bf1…`, dev-task
  manifest `163e1c6e…`; dev-spec is 100 items (89k tokens), valid 795.
- **task**: 263 programs written by agent lanes from topic lists. Each has a spec, an AIL program, an independent Python
  reference and five stdin cases whose expected output the Python reference produces; kept only when the AIL program
  matches it exactly on every case.
- **Harvest**: 112 of 240 whole-program tasks were sampled from the run 1 ~7B; agent lanes wrote minimal edits of its
  failing programs, each kept only when the compiler confirmed it passes and prints the expected output and it stays
  close to the draft (similarity at least 0.50): the 131 repair and behave items.

### Training

QLoRA on the 4-bit base, rank 32 on every linear layer, sequence 4,096, batch 1 x 16 accumulation, learning rate 1e-4,
1 epoch: 1,488 steps in 8.7 hours (07:21 to 16:06 UTC), 20.5 s per step, 847 tokens per second in the speed check
(peak 6.7 GB there; 11.2 GB reserved during the run, the overflow spilling to shared memory). Validation loss
**0.1585, 0.1487, 0.1438** at steps 500, 1000 and 1488; the final weights are the best checkpoint. Run 1 reached 0.139
at the end of its first epoch on its smaller data set, against the same validation split.

### A faster eval path

Run 3 is scored on the PC with llama.cpp: each model merged, converted to GGUF Q4_K_M (4.7 GB) and served with 6
parallel slots of 6,144 tokens, 8 items in flight, `ail check` running alongside (`tools/pc/run.sh serve`, then
`BACKEND=server`). Same prompts, seeds, 3 samples at temperature 0.2, 1,536 tokens, same pass rule; top-k and the
repetition penalty come from the base model's generation config. A full quick eval takes **13.5 minutes instead of
122** (about 9x faster).

Scores on this path are **not comparable with the NF4 rows above**: the run 1 final weights score 51.8 here against 53.8
on NF4. Most of the gap is in complete (30.1 against 43.0). The answers are well-formed in both (fences, indentation,
no truncation); the code itself differs, which points at the 4-bit weight format and sampler details, not the harness.
Both run 3 models below are scored on this one path. A check with the repetition penalty off and a Q6_K GGUF is in
[complete on the server path](#complete-on-the-server-path).

### Quick eval

pass@1 in percent (compile rate in brackets), server path. Baseline: run 1 final weights. Loop: up to 3 `ail check`
correction rounds, as in arm B.

| Family | Baseline | Run 3 | Baseline + loop | Run 3 + loop |
|---|---|---|---|---|
| fixline | 96.9 (96.9) | **100** (100) | 100 (100) | 100 (100) |
| fix | 94.0 (94.0) | **96.4** (98.8) | 97.6 (97.6) | 95.2 (98.8) |
| cursor | **71.9** (100) | 64.6 (94.8) | **72.9** (100) | 65.6 (96.9) |
| complete | 30.1 (84.9) | **37.6** (76.3) | 29.0 (88.2) | **45.2** (89.2) |
| function | **46.2** (88.2) | 36.6 (86.0) | **46.2** (90.3) | 40.9 (92.5) |
| port | **28.1** (36.5) | 22.9 (31.2) | **39.6** (55.2) | 36.5 (47.9) |
| write | 0 (27.1) | 0 (27.1) | 0 (46.9) | 0 (52.1) |
| **All** | **51.8** (74.9) | **50.5** (72.9) | **54.4** (82.3) | **54.1** (82.1) |
| pass@3, all | 55.5 | 55.5 | 58.7 | 57.8 |

The one-shot columns are separate runs; each loop run repeats its own round 0 (baseline 51.4, run 3 51.7), so the gain
from the loop is measured against that.

- **Level overall.** 50.5 against 51.8 one shot and 54.1 against 54.4 with the loop, within noise at 218 items.
- **Run 3 moved strength between families**: complete +7.5 (+16 with the loop), fix and fixline to 96 to 100; cursor
  −7, function −10, port −5.
- **write is still 0** in every column.

### dev-spec

100 programs held out by group: the task line and the exact expected output, the whole program to write.

| | Baseline | Run 3 | Baseline + loop | Run 3 + loop |
|---|---|---|---|---|
| compile | 36.0 | 38.0 | 60.3 | 56.7 |
| pass@1 | 0.3 | 1.0 | 0.3 | 1.3 |
| pass@3 | 1.0 | 2.0 | 1.0 | 2.0 |

dev-spec gives the output but not the sample data the reference program embeds, so a correct program can get the
shape right and every number wrong: of the compiled-but-wrong answers, most print the right number of lines with
different values in almost every line. It under-specifies the task the way write does, so it is a weak measure of
whole-program skill. dev-task replaces it.

### dev-task: held-out input-driven programs

61 new tasks in `data/eval/dev-task/` (eval only; its manifest hash is in `data/splits.sha256`, and the build fails if
any of its specs or programs appears in training data). Each has a complete spec (input format, rules, output format,
edge cases, one worked example), an AIL reference, an independent Python reference and 3 to 5 stdin cases. Topics
differ from the training tasks, and no program or spec shares more than 26% of its 8-grams with any training,
quick-eval, valid, dev-spec or training-task text. Sizes by the reference program: 20 small (10 to 24 lines), 26 medium
(25 to 60), 15 large (61 to 120, several functions, structs or enums, error handling).

The prompt is the training `task` format: the spec and two example cases. A sample passes only when it passes
`ail check` and prints exactly the expected output on **every** case (`tools/eval_devtask.py`, `run.sh devtask`).

| Size | Items | Compile, baseline → run 3 | pass@1, baseline → run 3 | pass@3, baseline → run 3 | + loop: pass@1 | + loop: pass@3 |
|---|---|---|---|---|---|---|
| small | 20 | 45.0 → 56.7 | 3.3 → **8.3** | 5.0 → **15.0** | 10.0 → 15.0 | 20.0 → 25.0 |
| medium | 26 | 39.7 → 55.1 | 0 → **3.8** | 0 → **7.7** | 2.6 → 3.8 | 7.7 → 7.7 |
| large | 15 | 11.1 → 20.0 | 0 → 0 | 0 → 0 | 0 → 0 | 0 → 0 |
| **All** | 61 | **34.4 → 47.0** | **1.1 → 4.4** | **1.6 → 8.2** | 4.4 → 6.6 | 9.8 → 11.5 |

Compile after the loop: 58.5 → 66.7 (large 22.2 → 40.0). Of the cases run by compiled one-shot programs, the baseline
passes 24.6% and run 3 38.1%.

- **Run 3 writes more whole programs that work**: one shot 4x pass@1 and 5x pass@3, and its one-shot score equals the
  baseline with three rounds of compiler feedback. At 61 items each item is about 1.6 points of pass@3, so the gain is
  about four more tasks solved: real, modest.
- **The loop narrows the gap** (6.6 against 4.4) because the baseline gains more from it.
- **Large programs are unsolved** by both.

### Compiler feedback: recovery and cost

| | Quick eval, baseline | Quick eval, run 3 | dev-spec, baseline | dev-spec, run 3 | dev-task, baseline | dev-task, run 3 |
|---|---|---|---|---|---|---|
| Samples failing `ail check` at first | 173 | 172 | 192 | 186 | 120 | 97 |
| ... compile after the rounds | 32.9% | 32.0% | 38.0% | 30.1% | 36.7% | 37.1% |
| ... then pass | 11.6% | 9.3% | 0% | 0.5% | 5.0% | 4.1% |
| Error recurrence | 75.4% | 83.2% | 75.1% | 82.9% | | |
| Unchanged revisions | 38.3% | 58.1% | 37.3% | 51.6% | | |
| Tokens per sample, one shot → loop | 963 → 2,572 | 962 → 2,611 | 855 → 4,070 | 789 → 3,587 | | |
| Seconds per sample, one shot → loop | 5.0 → 23.0 | 5.1 → 23.5 | 8.7 → 47.2 | 7.9 → 39.2 | | |

Error recurrence and unchanged revisions as in arm B. Passes by correction round on the quick eval: baseline 336, 16, 0,
4; run 3 338, 11, 3, 2.

- **No gain in recovery.** Run 3 recovers its compile failures no better than the baseline and repeats itself more:
  more recurring diagnostics, and more revisions returned unchanged (58% against 38% on the quick eval). Its 2,061
  repair items use the loop's correction prompt but are single-round, mostly injected faults; only 36 come from the
  model's own failures, and none are multi-round transcripts.
- The loop costs about 2.7x the tokens and 4.6x the time per sample on the quick eval, 4.5 to 5x on dev-spec.

### Where it fails

From a re-run of every saved dev-spec and quick-eval answer with the pinned compiler (2026-11-25):

- **Compile failures** start most often with `expr.name.1` (an unknown name: 47 of 188 failing run 3 samples, 44 of 197
  baseline). Run 3 almost stopped getting `main` wrong (`mod.main.1` 14 → under 5) but trips on newer constructs:
  `trait.op.3`, `lex.str.7` (format specifications), `err.prop.*`, `type.enum.2`. About 70% of failing samples have more
  than one error.
- **Compiled but wrong** (dev-spec): runtime traps 26 (baseline 20), right line count with wrong values 42 (43), very
  different output 40 (38), formatting only 1 (2), empty output 0.
- **Program length**: on programs over 40 lines run 3 compiles far more often than the baseline (36% against 22%), but
  less often at 20 to 40 lines (41% against 51%).
- **Quick-eval losses**: function regressions are mostly output differences (4 samples formatting only); port
  regressions are mostly compile errors (call shapes, unknown names, immutable bindings, field access on an optional
  without unwrapping).

### complete on the server path

The baseline's 31 complete items, 3 samples each, server path:

| Setting | Compile | pass@1 | pass@3 |
|---|---|---|---|
| NF4, transformers (PC cross-check) | 88.2 | **43.0** | 48.4 |
| Q4_K_M, usual sampler | 84.9 | 30.1 | 38.7 |
| Q4_K_M, repetition penalty off | 80.6 | 36.6 | 45.2 |
| Q6_K, usual sampler | 81.7 | 34.4 | 38.7 |

Each change recovers part of the gap (about 6 and 4 points), within the noise of 93 samples, and neither closes it;
the other server-path rows were not re-scored. Compare server-path rows with each other only.

### What run 3 says

- **Level on the quick eval**, with strength moved from cursor, function and port to complete and fixing.
- **Better one-shot whole programs from a full spec**: dev-task pass@1 1.1 → 4.4 and pass@3 1.6 → 8.2, compile 34 →
  47%, and compiled programs pass more of their cases. This is the first measurable whole-program gain.
- **No gain in recovery from compiler feedback**; run 3 repeats its diagnostics more often.
- **Large programs are unsolved** (0 of 15 for both models, under half compiling).

| Mac reference, 4-bit MLX | Quick eval pass@1 | dev-task pass@1 | dev-task pass@3 |
|---|---|---|---|
| ~7B run 1 final | 52.4 | *pending* | *pending* |
| ~7B run 3 final | *pending* | *pending* | *pending* |

Run on the PC 2026-11-25. Results (summaries, every answer and revision, the failure digest) are on the share in
`ail-train/pc-evals/run3/`; the merged model, its GGUF and the adapter in `ail-train/pc-run3-7b-final/`.

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
| ~7B final, 4-bit | `eval-M-20261123T231410Z` |

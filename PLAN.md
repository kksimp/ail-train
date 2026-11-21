# ail-train plan: teach a small local model AIL

Written 2026-11-20. This file is self-contained: a new project or agent should be able to start from it plus
[CONTEXT.md](CONTEXT.md) without the old AIL project's history. Decisions marked **(Kaleb)** were made by the
designer and are not reopened without him.

## 1. Goal

1. **Proof.** Show that training data, not language changes, closes the agent-unfamiliarity gap that the AIL agent
   benchmarks measured (fresh tasks, frontier agent: first-correct 56/80 in AIL against 70/80 in C, 1.35 versions to
   correct against 1.12). Here the same idea is tested cheaply: one small model, before and after training on AIL.
2. **Product.** The tuned model backs an optional, local, offline AIL helper in ail-edit: explain a diagnostic,
   propose a fix, draft a function.

Not goals: beating C, matching a frontier model, or changing AIL syntax (standing rule: no syntax changes to mimic
other languages; teach through docs, diagnostics and auto-fix).

## 2. Decisions so far

| # | Decision | By |
|---|---|---|
| D1 | First run: a ~1.5B-parameter base at 4 bits with LoRA. Try ~3B only after the 1.5B result is in. | Kaleb |
| D2 | The E14/final-run agent programs and drafts are training data, minus every task in the new eval pool. | Kaleb |
| D3 | All scripts live in this private repo (kksimp/ail-train), not in kksimp/ail. Data built from them and adapters stay out of git. | Kaleb |
| D4 | Pass bar: the tuned model's first-correct rate is at least **2x** the same model untrained, **and at least 25%** of trials, on fresh sealed tasks (floor added 2026-11-20). | Kaleb |
| D5 | ail-edit: an optional setting that points at a local model, **off by default**, Mac first, shown as unavailable on Linux and Windows. | Kaleb |
| D6 | No model or model identifier is written into any committed file. The base model is named only in the untracked `config.local` on the Mac and in chat. | standing rule |
| D7 | Everything runs on Kaleb's machines, never in a cloud container, and costs nothing (no paid API). | standing rule |
| D8 | Training starts only after AIL 0.2.0 is tagged and Kaleb says go. | Kaleb |
| D9 | The core card stays as the system prompt on every training example (2026-11-20). The sequence cap rises to about 4096 to hold it; the preflight measures memory and speed at that length. | Kaleb |
| D10 | The M1 preflight measures three candidate sizes, about 1.5B, 3B and 4B, each at the D9 sequence length; the base is picked from the measured numbers (2026-11-20). D1's order still holds unless that card says otherwise. | Kaleb |
| D11 | Grow the training set to about 3,000 distinct compiler-checked programs (2026-11-20). Project threads write them in batches under `data/extra/`; the Mac checks each with `tools/check_extra/run.sh`; only passing programs are kept. No paid service. | Kaleb |

Open (ask Kaleb with a tappable card when reached): which concrete base model (section 4), whether a published
adapter is wanted at all (licence, section 4), whether the eval report goes on the public AIL benchmarks page.

## 3. Hardware budget

- **Mac** (M2 MacBook Pro, 8 GB unified memory). Hard cap for this work: 6 GB. Start a heavy job only while load
  average < 8, one heavy job at a time, back off past ~12 or when free disk < 20 GB. MLX runs only here.
- 1.5B at 4 bits: ~1 GB weights; LoRA rank 16 plus optimizer state is small; with batch 1, sequence 2048 and
  gradient checkpointing the expected peak is 3-4 GB. Measure it in the preflight; abort above 6 GB or on swap.
- ~3B at 4 bits: ~2 GB weights, expected peak 5-6 GB at sequence 1024. Only after D1's first result.
- 7B and above: does not fit.
- **ail-linux / ail-win** VMs: used only to re-check data on the other hosts if needed (`ail check` agrees on all three
  hosts by the parity rule). No training there.
- Speed is unknown until measured. Planning figure: a few hundred tokens per second, so ~1M training tokens is about an
  hour per epoch. A full 3-epoch run should fit in one evening.

## 4. Base model choice (card for Kaleb at milestone M1)

Criteria, in order:
1. Fits D1 (1-2B, an MLX 4-bit build exists).
2. Code-trained instruct model with a chat template (needed for the fix and port tasks).
3. **Licence.** Apache-2.0 or MIT preferred. Some small bases ship under research-only or custom licences that forbid
   bundling or redistribution; such a base may be used for the private proof but not for an ail-edit download.
   Publishing or bundling an adapter is a licensing question for Kaleb (AIL escalation rule 4).
4. Tokenizer cost on AIL source (measure on 20 corpus files; fewer tokens per program means more examples per
   sequence and faster inference).

M1 presents two or three concrete candidates on a decision card with measured memory, speed and tokens-per-program.

## 5. Data

Everything AIL that enters training must pass `ail check` with the AIL 0.2.0 compiler, and every program with a known
expected output must reproduce it. The builder drops failures and reports counts.

### 5.1 Sources

| Source | Where | Size | Becomes |
|---|---|---|---|
| Corpus programs with Python twins | kksimp/ail `corpus/NAME/{NAME.ail,NAME.py,NAME.out}` | 302 programs, ~890 KB AIL | `write` (task text -> program) and `port` (Python twin -> AIL) |
| Mistake triples | kksimp/ail `tests/mistakes/NAME.{ail,fixed,rules}` | 271 pairs | `fix` (wrong program + diagnostic -> fixed program) |
| Examples | kksimp/ail `examples/*.ail` + `.out` | 90 | `write` |
| Test cases | kksimp/ail `tests/cases/*.ail` | 852 files | `complete` (filtered: drop fuzz, limits, native-only and error-expecting cases unless used as `fix`) |
| Agent final programs | this repo `data/raw/trials.jsonl` | 333 AIL trials (320 correct), 16 tasks | `write` (SPEC.md -> program) and `change` (seed + issue -> program) |
| Agent failing drafts | this repo `data/raw/drafts.jsonl` | 340 failed versions with the diagnostics they got | `fix` (draft + fresh diagnostic -> the trial's final correct program, when the diff is local) |
| Docs | kksimp/ail `docs/language-card.md` (~16k tokens), `docs/language-card-core.md` (~3k tokens), `docs/how-to.md`, `llms-full.txt`, `docs/quick-reference.md` | ~95 KB | the core card is the system prompt; how-to rows become short Q&A |
| Doc snippets | `ail` blocks in kksimp/ail `docs/` (checked by `tools/check-doc-snippets.py`) | hundreds | `complete` |
| Explain texts | `ail explain RULE` for every rule ID | a few hundred | `explain` (diagnostic -> cause and fix) |
| Drill programs with Python twins | this repo `data/extra/drills/NAME/{NAME.ail,NAME.py,NAME.out}` | 40 programs, ~56 KB AIL | `write`, `port`, `complete`; each targets built-in methods the corpus uses under five times and the top draft mistakes (see `data/extra/README.md`) |
| D11 batches with Python twins | this repo `data/extra/batchNN/NAME/{NAME.ail,NAME.py,NAME.out}` | 600 programs so far (batch01 to batch06), growing to ~2,570 | `write`, `port`, `complete` |
| Future public corpus | planned after 0.2 in kksimp/ail | - | same families; retrain when it lands |

The agent programs are agent-written and correct by the benchmark's hidden cases, so they teach the shape of real
tasks. The drafts show the exact mistakes frontier agents make in AIL (see `data/raw/draft-error-lines.txt`: unknown
std methods such as `trim_start_chars`, unhandled failures `err.use.1`, block shape `expr.block.2`, ...). That is the
gap this project targets.

### 5.2 Task families and format

Chat JSONL, one object per line, the format `mlx_lm.lora` reads:
`{"messages": [{"role":"system","content":CORE_CARD}, {"role":"user","content":...}, {"role":"assistant","content":...}]}`

| Family | User turn | Assistant turn |
|---|---|---|
| write | the task (corpus header comment, SPEC.md, or example description) | the full program |
| port | "Port this Python program to AIL" + the twin | the AIL program |
| fix | the program + the exact `ail check` output from the 0.2 compiler | the corrected program (whole file; diffs later) |
| change | the seed program + the issue text | the changed program |
| explain | a diagnostic line | cause and fix in two or three sentences (from `ail explain`) |
| complete | the program with one function body removed | the body |

Target mix by tokens (adjust after the first run): write 35%, fix 25%, port 15%, change 10%, complete 10%, explain 5%.
Optional later: ~10% general code instruction data under a permissive licence, to limit forgetting.

System prompt: the **core card** (~3k tokens), not the full card. The full card does not fit at sequence 2048 on 8 GB,
and the model should carry the language in its weights. Examples longer than the sequence cap (about 4096, D9) with the core card are
split (multi-file tasks) or dropped and counted.

### 5.3 Contamination rules

1. The post-training eval uses **new tasks authored after the data freeze** (M3), sealed on the Mac in
   `~/ail-heldout/train-eval/`, never in git, never in the cloud. The author does not see the training set.
2. `heldout_spent: true` in the raw files marks the old held-out tasks (`calc`, `invjson`, `maze`). They were already
   used for one eval and are allowed as training data, never as eval tasks.
3. The 2026-11 sealed tasks of the final run and the $40 rerun stay only on the Mac (`~/ail-heldout`, `~/ail-final`).
   They are not used for training or eval.
4. Split by task, not by file: a held-out quick-eval split (10% of corpus tasks, 10% of mistakes) is chosen with a
   fixed seed and written to `data/build/manifest.json`.
5. Near-duplicate filter: drop any training program whose normalised token 8-gram overlap with an eval program is
   above 30%.

### 5.4 Builder

`tools/build_data.py` (to write in M2), run on the Mac:
- inputs: an ail checkout at the 0.2.0 tag (path argument), this repo's `data/raw/`;
- runs the tree's `ail check` (and `ail run` where an `.out` exists) on every program, records the output;
- emits `data/build/{train,valid,quick-eval}.jsonl` and `manifest.json` (counts per family and source, token
  totals with the chosen tokenizer, ail commit, seed, dropped items and reasons);
- deterministic: same inputs give byte-identical output.

## 6. Training recipe (first run)

- `mlx_lm.lora --train` with LoRA on attention and MLP projections, rank 16, scale 32, 16 layers, batch 1 with
  gradient accumulation 8, `--grad-checkpoint`, max sequence about 4096 (D9), learning rate 1e-4 cosine with warm-up, 2-3 epochs,
  validation every 100 steps, adapters saved every 200 steps, `--mask-prompt` (loss on the answer only).
- Stop early when validation loss rises for two evaluations.
- After training: `mlx_lm.fuse` to a standalone model; keep the adapter too.
- Every run writes `runs/STAMP/{config.json,log.txt,val.jsonl,mem.txt}` under `~/ail-train-work/` on the Mac and a
  short summary file the thread can read.

## 7. Evaluation

Arms (same tasks, same harness, same sampling settings):
- **A** base model + core card in the prompt
- **B** base model + as much of the full card as fits (recorded)
- **C** tuned model + core card

Stages:
1. **Quick eval** (minutes): the quick-eval split. Corpus tasks: compiles, and output equals `.out`. Mistakes: the
   answer compiles and behaves as `.fixed`. Metrics: compile rate, pass@1, pass@3 (temperature 0.2, 3 samples).
2. **Loop eval** (the benchmark metric): reuse kksimp/ail `tools/agentbench/agentbench.py` with
   `AGENTBENCH_AGENT` pointing at a local agent (`tools/local_agent.py`, to write in M4) that speaks the same CLI
   contract as the fake agent in `tools/agentbench/fake/agent.sh`: accepts `-p`, `--model`, `--max-budget-usd`,
   prints stream-json, reports cost 0. Inside, a simple loop: read SPEC.md, write `src/main.ail`, run `./build` and
   `./test`, feed the output back, up to 8 attempts. agentbench then computes `first_check_clean`,
   `versions_to_green`, correctness on hidden cases, exactly as for the frontier runs.
3. **Fresh sealed tasks** (D4): 12-20 new from-scratch tasks in agentbench format with AIL reference solutions,
   authored in M3. 5 trials per task per arm.

Pass bar (D4): arm C first-correct >= 2 x arm A first-correct, and >= 25% of trials, on the sealed tasks. Also report final-correct and
mean versions to correct, beside the frontier figures from CONTEXT.md, with the caveat that a 1.5B model is not
expected to match a frontier model. A failed bar is still reported honestly; it tells us whether data volume or
model size is the limit.

## 8. ail-edit integration (after the eval, D5)

- Serve with `mlx_lm.server` (OpenAI-compatible, 127.0.0.1) started on demand, or one-shot `mlx_lm.generate`.
- ail-edit gets a setting `helper.endpoint` (empty = off). The ask bar sends: the selection, current
  `ail check --json` diagnostics for the file, and the core card. The reply is shown as a diff; on accept the editor
  re-runs `ail check`.
- Linux and Windows show the setting as "Mac only for now", never fail silently (feature-parity rule).
- Work lands in kksimp/ail-edit through its own lane, following its plan (one module per feature under
  `features/NAME/`, one key row, one dispatch line).

## 9. Milestones

Each heavy step is one job on the Mac, one at a time, within the section 3 limits. Each milestone ends with a short
report in the thread and its checkboxes updated here.

- **M0 Plan and raw data** (done 2026-11-20): this file, CONTEXT.md, `data/raw/`, `tools/extract_trials.py`.
- **M1 Preflight** (Mac, ~30 min). Self-setting-up `tools/preflight.sh`: Python venv in `~/ail-train-work/venv`,
  `pip install mlx-lm`, record chip, macOS, free memory and disk; download three candidate bases at 4 bits, about 1.5B, 3B and 4B (D10); tokenise 20
  corpus programs per candidate; a 50-example, 20-step LoRA smoke run per candidate recording peak memory and tok/s.
  Done when: a decision card with the measured numbers is answered (base model chosen).
- **M2 Data builder.** `tools/build_data.py` as in 5.4; Mac job against ail 0.2.0. Done when: manifest counts
  reported, every kept item passed `ail check`, and the deterministic rebuild matches.
- **M3 Fresh eval tasks** (separate lane, must not read `data/`). 12-20 tasks in agentbench format, AIL reference
  solutions validated with `agentbench.py validate` on the Mac, sealed in `~/ail-heldout/train-eval/`. Can run in
  parallel with M2.
- **M4 Local agent + baseline.** `tools/local_agent.py`; run arms A and B on the quick eval and on the sealed tasks.
  Done when: baseline table recorded.
- **M5 First training run** (1.5B). Done when: adapter saved, val loss curve, quick-eval table A/B/C.
- **M6 Loop eval on sealed tasks**, arm C. Done when: the D4 verdict and the full table are reported.
- **M7 Decide** (card): 3B run, more data, or go to ail-edit integration.
- **M8 ail-edit helper** (if M7 says so).

## 10. Repository layout

```
AGENTS.md, CLAUDE.md     rules for AI agents working here (CLAUDE.md imports AGENTS.md)
LICENSE                  AGPL-3.0
PLAN.md                  this plan
CONTEXT.md               everything a new project needs to know about AIL, the machines and the rules
data/raw/                committed raw inputs from the AIL project (see data/raw/MANIFEST.md)
data/build/              builder output (git-ignored)
tools/extract_trials.py  pulls AIL trials out of agentbench result archives
data/extra/              programs written for training (drills); checked on the Mac by tools/check_extra/run.sh
tools/preflight.sh       M1 (to write)
tools/build_data.py      M2 (to write)
tools/local_agent.py     M4 (to write)
tools/eval_quick.py      M5 (to write)
config.local             untracked: base model id, paths (D6)
```

## 11. Risks

- **Small data** (~1-1.5M tokens): overfitting. Keep the validation split, stop early, add the public corpus later.
- **Card memorisation** instead of language learning: the port, fix and change families force real use.
- **Python-shaped AIL** from port tasks: the quick eval and loop eval catch non-idiomatic code by compile errors;
  keep port at 15%.
- **Stale diagnostics**: the drafts carry diagnostics from older compilers; the builder regenerates them with 0.2.0.
- **Memory**: swap makes training crawl and starves the gate. Never train while a gate runs on the Mac.
- **Licence** of the base blocks bundling (section 4).
- **Language drift** after 0.2: the manifest pins the ail commit; rebuild and re-validate data on each AIL release.

## 12. Review of 2026-11-20 (8 GB methods)

Findings from a review of this plan against current published methods. Kaleb answered the four decisions on 2026-11-20 (D4 floor, D9, D10, D11).

- **The core card does not fit the sequence.** The core card is ~3k tokens and the sequence cap was 2048, so with the
  card as the system prompt every example was over the cap. Decided (D9): keep the card on every example and raise
  the cap to about 4096. Cost: roughly double the activation memory and step time of 2048, so the preflight must
  measure the peak at 4096 for each candidate, and a base that passes 6 GB at that length is out. Sections 3, 5.2
  and 6 read "2048" as "about 4096" from here on. Rejected: a short prompt with the card on a minority of examples.
- **Model size.** Published low-resource-language results: a 1B base gained 3.5 to 8 points of pass@1 from ~40k
  verified examples per language (arXiv 2308.09895); a reinforcement method gained nothing at 1.7B and 3B and gained
  clearly at 4B (arXiv 2508.04865). On-device work trains a 4B base at 4 bits on 8 GB phones under ~1 GB at sequence
  256 with exact gradients (arXiv 2510.03425). Decided (D10): the M1 preflight measures 1.5B, 3B and ~4B candidates.
- **Pass bar.** An untrained small base writes almost no correct AIL, so "2x the base" alone could be met by a model
  that is still unusable. Decided: D4 keeps 2x and adds a floor of 25% first-correct. Rejected: 2x only; a 50% floor.
- **Data volume.** The training set holds about 1,000 distinct verified programs (the 333 agent trials cover 16
  tasks). The cited work used tens of thousands, and found unverified data useless or harmful, so growth must go
  through `ail check` and expected output. Decided (D11): grow the set to about 3,000 compiler-checked programs. Each batch is checked on the Mac before the next
  is written, so the failures of one batch correct the next. Rejected: stopping at the 40 drills; waiting for the public corpus.
- **Coverage.** Of the methods the language card names, most appear under five times in the corpus and examples
  (`center`, `rfind`, `get_or`, `map_values`, `zip`, `windows`, `chunks`, `flatten`, `take_while`, `checked_*`, ...).
  Guessed method names are the top draft error. `data/extra/drills/` starts to close this; `tests/cases/*.ail` with
  a `.out` (470 files) already exercises every method and should also feed a `predict output` family.
- **Memory settings for the first run** (no decision needed; confirm flag names in the preflight): batch 1 with
  gradient accumulation, gradient checkpointing, loss on the answer only, examples sorted into length buckets,
  sequence cap chosen from the token histogram instead of a fixed 2048, LoRA on the last 8 to 16 layers only (a
  shorter backward pass), no other heavy app open, abort on swap. Second run only if the first shows headroom:
  DoRA, and a loss computed in chunks.
- **Not adopted now.** Hand-written memory-efficient backward passes (arXiv 2602.13069, 2510.03425) need custom code
  for a saving the settings above mostly reach. Reinforcement training with compiler reward is a candidate after M6.

## 13. Rejected alternatives

- Full fine-tune: does not fit 8 GB.
- The full card in every example: too long for 8 GB and teaches the card text more than the language.
- Cloud GPUs or a paid fine-tuning API: forbidden (D7).
- Training on the sealed tasks: would make the proof worthless (5.3).
- Scripts inside kksimp/ail: Kaleb chose a separate repo (D3).
- A 7B+ model on the Mac: does not fit; the 2026-10 attempt with a large mixture-of-experts model streamed from disk
  ran at ~4 tok/s and still wrote non-AIL syntax (CONTEXT.md, "Prior local model attempt").

# Context for ail-train

Everything a new project or agent needs that is not in [PLAN.md](PLAN.md). Facts as of 2026-11-20.

## People and roles

- **Kaleb** (GitHub `kksimp`) is the designer of AIL and owner of this repo. US Eastern time. He skims from a phone:
  ask every question as a tappable card with options, the recommended one first, never as a prose list.
- The AI implements and plans. It decides routine questions itself and escalates anything that involves money,
  licences, publishing or accounts, or that changes a decision Kaleb made.

## Licence

This repo is AGPL-3.0 (`LICENSE`, the same text as kksimp/ail-edit), decided by Kaleb on 2026-11-20. It covers
the scripts, plan and committed data. AIL itself stays Apache 2.0; a base model and any adapter keep their own
licence questions (PLAN.md section 4).

## AIL in one paragraph

AIL (AI-First Language, by Voltare) is a native, garbage-collected, memory-safe systems language with
indentation-based syntax, written so humans and AI agents are both first-class programmers. Repo: kksimp/ail
(Apache 2.0 with a Runtime Library Exception). The compiler is self-hosted in AIL. CLI: `ail check`, `ail run`,
`ail build`, `ail test`, `ail fmt`, `ail explain RULE`, `ail fix`. Diagnostics carry spec rule IDs such as
`expr.name.1` or `err.use.1`. Version 0.1.0 shipped 2026-11-15. 0.2.0 is in release on 2026-11-20 (pin this project's
data to the 0.2.0 tag). Read in kksimp/ail: `docs/language-card-core.md` (the short card), `docs/language-card.md`
(the full card), `docs/how-to.md`, `docs/for-agents.md`, `llms-full.txt`.

Traps agents hit most (from the drafts in `data/raw/`): guessed std method names (`trim_start_chars`, `pad_left`),
unhandled fallible calls (`err.use.1`), block shape (`expr.block.2`), unknown types from other languages.
Language traps: `error`, `par`, `any`, `with`, `unique` are keywords; `elif`; no `+` on strings or lists;
`to_int()` returns an optional; `Task` is built in.

## The gap this project targets

Agent benchmark history (kksimp/ail `tools/agentbench`, ADR 0916; reports in `data/raw/reports/`):
- E14 full run (2026-11-17, 840 trials): AIL arms behind C on first drafts; held-out task `calc` hit AIL hardest.
- Final run (2026-11-19, frozen 978793e8, 464 trials): NOT MET. 32 AIL first drafts did not compile against 4 for C;
  almost all were a guessed std name or a habit from another language. Once AIL compiled, logic errors were rarer than
  in C (1 failed visible-test version against 14).
- $40 rerun (2026-11-20, frozen 767759a3, 8 fresh sealed tasks): ail-plain 78/80 correct vs C 79/80, first version
  green 56/80 vs 70/80, mean versions 1.35 vs 1.12, AIL ~20% cheaper per trial. Called "lost" on tries. Kaleb's note:
  results are expected to improve much once models pick up AIL; this was first contact.

So the gap is unfamiliarity in the first draft, not correctness. This project tests whether training data fixes it.
Public wording rule: be honest that agents are less efficient in AIL until models learn it; never claim AIL is "close
to C" or "rivals C" in speed; say "fast and efficient".

## Prior local model attempt (2026-10-22, paused)

A large mixture-of-experts coder at 4 bits was streamed from the internal SSD on the same Mac (setup in `~/ail-llm`,
launchd job `com.ail.localllm`, 127.0.0.1:8080, ~4 tok/s, now unloaded; `~/ail-llm/RESUME.md` restarts it). With no
AIL training it passed one-line anchored edits (3 of 3) and failed multi-site edits (1 of 4): it wrote braces and
Python slices. Queue and loop rules used: `data/raw/prior-local-llm/browser-queue-1.md`. That is the untrained
baseline behaviour this project should beat, at a fraction of the size. The Python in `~/ail-llm` may be reusable.

## Machines

| Machine | Use | Notes |
|---|---|---|
| Mac (M2 MacBook Pro, 8 GB, Apple Silicon) | all training and MLX inference; `ail check` for data validation | Repos under `/Users/macintosh/Documents/Projects/` (ail is there). Work dir for this project: `~/ail-train-work/` (durable, not /tmp). `/Volumes/mac.apk` is a slow USB stick: never use it. bash 3.2, no `date +%s.%N`. |
| ail-linux (192.168.4.145) | optional cross-host `ail check` | VM on Kaleb's TrueNAS box, user kaleb, key `~/.ssh/ail_lanes`; shares the host with ail-win, so run jobs there serially |
| ail-win (192.168.4.148) | optional | PowerShell 5.1 |

Mac limits (Kaleb): AIL work max 6 GB of the 8 GB; start a heavy job only while load < 8, one heavy job at a time,
back off past ~12 or when disk < 20 GB. The AIL project gates on this Mac too: never train while a gate runs.

## Rules that carry over

- All builds, tests and training on Kaleb's machines, never in a cloud container. No paid API or paid service.
- No AI model name or model identifier in any committed file (base model id goes in untracked `config.local`).
- Anything Kaleb runs by hand must be one self-setting-up script: `run.sh` (macOS/Linux) or `run.ps1` (Windows),
  pasted from the repo root.
- Never rely on files in /tmp; keep helper scripts and outputs in durable folders.
- Verify a job is really running on the machine; don't trust a start message.
- Ask Kaleb before anything public, irreversible, paid, or licence-related (publishing an adapter, bundling a model).
- Never store PINs or passwords; secrets stay in the Mac Keychain.
- Git: work on a short-lived branch, merge through a pull request.

## Where the source data lives

- In this repo: `data/raw/` (see its MANIFEST.md).
- In kksimp/ail (read-only for this project; add the repo to the new project): `corpus/`, `tests/mistakes/`,
  `examples/`, `tests/cases/`, `docs/`, `llms-full.txt`, `tools/agentbench/` (harness, tasks, fake agent).
- On the Mac only: full agentbench results with transcripts (`~/ail-final/results`, final run and rerun), the sealed
  tasks (`~/ail-heldout`, never read by a data-building lane), the old project's job logs.
- Larger archives (transcripts of E13/E14 runs, ~60 MB) stayed in the old AIL project's shared files; the AIL source
  in them is already extracted into `data/raw/trials.jsonl`.

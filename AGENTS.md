# AGENTS.md

ail-train teaches a small local model AIL (LoRA, MLX, Apple Silicon). Read [PLAN.md](PLAN.md) for goals, decisions and
milestones, and [CONTEXT.md](CONTEXT.md) for AIL, machines and rules. Licence: AGPL-3.0.

- Builds, data checks and training run only on Kaleb's Mac (or the ail-linux and ail-win VMs for `ail check`), never in
  a cloud container. No paid API or service.
- Never write a model name or model identifier into a committed file; the base model lives in untracked `config.local`.
- Anything Kaleb runs is one self-setting-up `run.sh` or `run.ps1`, pasted from the repo root.
- Built data, adapters and runs stay out of git (`.gitignore`).
- kksimp/ail and kksimp/ail-edit are read-only from here: read them, file issues or PRs, never push to them.
- Git: `main` is the only long-lived branch. Work on a short-lived branch and merge through a pull request.
- Ask Kaleb, with a card, before anything public, paid, irreversible or licence-related.

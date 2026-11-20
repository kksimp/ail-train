# data/raw manifest

Raw inputs copied from the AIL project on 2026-11-20. Model names are removed from copied text (rule D6).

| File | What | Origin |
|---|---|---|
| `trials.jsonl` | 333 AIL agent trials (320 correct) on 16 tasks: run, task, arm, trial, metrics, the task's SPEC.md or issue.md, and every `.ail` file of the final workspace. `heldout_spent` marks `calc`, `invjson`, `maze`. | `tools/extract_trials.py` over the E13 pilot, E14 pilot/pilot2/confirm/calc-rerun, final pilot and final-run (non-sealed) result archives |
| `drafts.jsonl` | 340 failing AIL draft versions with source, the diagnostics they got (`base`, `intake`, `checkfix`: rule IDs and diag lines) and the trial key to join with `trials.jsonl` | replay of E13/E14 drafts on ail abde00560 |
| `draft-error-lines.txt` | the drafts' error lines grouped by rule ID, most common first | same replay |
| `reports/` | benchmark reports and reviews: rerun-40 report, final-run review, pilot review, E14 full reports, E14 review verdict, agent fluency, held-out losses, iterations, confirm and calc-rerun analyses | old project shared files |
| `prior-local-llm/browser-queue-1.md` | loop rules and tasks used in the 2026-10 local model attempt | old project shared files |

Not here on purpose: sealed task specs and their trials (Mac only), transcripts, C and Rust trials.

Join drafts to finals: `drafts.trial` (for example `e14-confirm-results/calc/ail-plain-10`) ends with
`TASK/ARM-N`; match it to `trials.jsonl` on task and `trial == ARM-N` and the run name prefix. 187 of the 340 drafts have their final in `trials.jsonl`; the other 153 do not
(their archive was not available); the builder drops those or uses them as
`explain` examples only.

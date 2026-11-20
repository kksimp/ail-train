# Paid pilot: independent double-check

Date: 2026-11-19. Read-only. Nothing built, launched or spent.
Inputs: `final-pilot-results.tgz` (42 `metrics.json`, `runs.jsonl`, build and test logs, transcripts, `spend.jsonl`),
`final-final-pilot-report.md`, `final-pilot-run.txt`, `final-run-forecast.md`, `final-run/forecast/sim.py`, and
`tools/agentbench/agentbench.py` at 4ecc5c8d.
Method: every figure recounted from the per-trial files with my own script; the bootstrap rewritten and rerun; the
forecast simulation rerun (3,000 runs, two seeds, each scenario). Hidden cases were not re-executed (no builds in the
cloud); I read the stored scores, the logs and the transcripts.

## Verdict

**The reported numbers hold. One figure is wrong (the spend) and three are true but flatter AIL if read alone.
Nothing here reverses the go/no-go, but the honest expectation for the full run is a miss, about 6 chances in 10.**

## 1. Recount

| figure | reported | recounted | |
|---|--:|--:|---|
| Trials, model, tree, agent CLI | 42, one model, 4ecc5c8d, 2.1.318 | same in all 42 | holds |
| AIL first version green | 18 of 21 (outline 7, wrap 7, tally 4) | same | holds |
| C first version green | 21 of 21 | same | holds |
| Correct on hidden cases | AIL 21 of 21, C 20 of 21 | same (C `tally` trial 2 fails `keyword`, 27 of 28) | holds |
| Mean versions to green | 1.14 against 1.00 (`tally` 1.43) | 24/21 = 1.143; `tally` 10/7 | holds |
| 95% interval of the gap | +0.00 to +0.33 | +0.00 to +0.29 (my resampling order differs; 6 or 7 of 21 at the edge) | holds |
| Builds that rewrote the source | 7 | 7 (`tally` 1, 3, 5, 7; `wrap` 2, 4, 6) | holds |
| Versions with a rewrite counted | 1.48 | 31/21 = 1.476 | holds |
| Cost per trial | $0.101 against $0.120 | $0.1009 against $0.1198 | holds |
| Cost without the DOCS read | $0.078 against $0.083 | same | holds |
| **Total spend** | **$4.53** | **$4.64** (sum of 42 trials and of `spend.jsonl`) | **wrong by $0.11** |

The $4.53 is the ledger before the last trial. Budget left is about $95.36 if $100.00 was exact before; check the
console balance before launch, not this arithmetic.

## 2. Scoring logic

Read in `agentbench.py` (`version_metrics`, `toolchain_metrics`, `score_ws`, `primary_table`, `target_table`). It does
what the report says. No bug found. Points a reader should know:

1. **"Green" means the 5 visible cases pass, not that the program is right.** Versions are counted up to the first
   passing `./test`. Correctness is scored separately on the final program against the hidden cases. Both arms are
   treated the same.
2. **AIL agents kept editing after green; C agents never did.** 4 AIL trials changed the source after the first green
   (`tally` 1, 3, 5, `outline` 4); 0 of 21 C trials did. Counting every version checked: AIL 1.33, C 1.00
   (interval +0.10 to +0.57). In `tally` 1 the first green version had a real bug (a literal over the range reported as
   `syntax`), which the agent found by its own edge test. The runner's rebuild confirms it: that first draft fails
   hidden cases. So `tally` 1 counts as "first version green" but was not first-version-correct. The verdict rule does
   not see this, and the report has no line for it.
3. **5 of AIL's 18 first-green trials were green only because the build repaired the draft.** Unaided clean first
   drafts: AIL 13 of 21 (`outline` 7, `wrap` 4, `tally` 2), C 21 of 21. The report states the 7 rewrites and the 1.48
   figure, so this is disclosed; but "`tally` 4 of 7" is 2 of 7 without repair.
4. **When the agent runs `./test` and not `./build`, it is not told the build rewrote its source** (the build output is
   deleted on success; `wrap` 2 and 4). No harm seen here. It could cause a stale edit in a longer trial.
5. Audit: `outside` lists `/item` (outline) and `/t` (tally 5). Both are text in commands (`</item>`, `\t`), not paths.
   No void trial. Correct.
6. `ail` reported itself as `...-g4ecc5c8d8-dirty`. The worktree had a modified or untracked file when the compiler was
   built. Probably a generated file, but confirm what it was before the full run, since the run commit must be exact.

## 3. Cost

"Cheaper" holds by the declared rule (total cost per trial). It rests on the DOCS size, not on less work:

| task | AIL total | C total | AIL without DOCS | C without DOCS | AIL output tokens | C output tokens |
|---|--:|--:|--:|--:|--:|--:|
| `outline` | 0.083 | 0.108 | 0.061 | 0.072 | 1,918 | 2,359 |
| `wrap` | 0.083 | 0.113 | 0.061 | 0.076 | 2,077 | 2,669 |
| `tally` (parser) | 0.137 | 0.139 | **0.112** | **0.101** | 5,495 | 4,648 |

On the parser task AIL is level on total cost and dearer without the DOCS read. The interval of the cost gap without
DOCS includes zero (-$0.017 to +$0.007). On the ordinary tasks AIL is cheaper both ways. For the full run the
"cheaper" line is still very likely to pass (C's card is 47 KB against 29 KB).

## 4. Forecast

- I reran `sim.py`: launch now 30%, after the fixes 43 to 44%, with a good parser recheck 53 to 55%. The stated 29, 41
  and 53% are reproduced (slightly conservative).
- The simulation applies the report's own rules (class "lost" when the lower bound is above zero, pooled upper bound
  under +0.10, correctness by interval). I found no mismatch with `agentbench.py`.
- Cost: 464 trials at the pilot's and E14's prices is $51 to $58. "About $55" is fair. The $78 cap fits in $95.
- **The weak link is the step from 29% to 41%.** It assumes the fixes cut a new parser task's first-draft failure rate
  from about 44% to about 28%. Nothing measures that. The three misses had three unrelated causes, and `calc` earlier
  showed that fixing the top causes exposes new ones. `tally` cannot test the fixes fairly any more, because they were
  written against it.
- The runner's rebuild with PR #1388 (drafts 6 and 7 fully correct; draft 3 compiles but fails one hidden case from its
  own logic) does not lower the 41%. The verdict counts versions to visible green, and all three drafts now reach it
  first time; in the paid trial the agent found draft 3's logic slip itself. It does show that "first version green"
  overstates "first version right" on parser tasks, the same point as 2.2.
- My own reading: **about 35 to 45% after the fixes**, most likely miss being "every class tied, pooled bound just over
  +0.10". With 232 trials an arm the observed gap must be about +0.04 or less to pass; the pilot's was +0.14.

## 5. Does anything change the go/no-go?

No error was found that changes it. By the rule fixed before the pilot (18 of 21 and no task under 5 of 7), the result
was "not as it stands", and the forecast said so. Launching after the three fixes is a defensible choice at roughly
4 chances in 10.

Before launch:
1. Correct the spend to $4.64 and read the real balance.
2. PR #1388 changes the compiler, so the run commit moves: gates, the 570-program replay, the task check and the dry
   run must be repeated on the new commit, and the pin in `final-job.sh` updated.
3. Find out why the pilot's compiler was `-dirty`.
4. Decide now how a miss will be worded. The secondary lines (1.48 with rewrites, cost without DOCS) will be quoted by
   any skeptic; add "versions checked in total" (1.33 against 1.00 here) so it is not found later by someone else.

Optional and cheap: 10 paid AIL trials of `calc` on the fixed tree (about $1.40). It is the only parser task the fixes
were not written against. 8 or more green supports the 41%; 5 or fewer says the parser gap is real and the full run
would most likely lose the held-out class.

---

# Update 2026-11-19 04:45Z: the `calc` check (10 paid AIL trials on 978793e8, with PR #1388)

Inputs: `calc-check-results.tgz`, `final-calc-check-report.md`, `calc-check-run.txt`. Same method as above.

## Verdict

**The check passed its bar (8 of 10 green first time; the bar fixed before the run was 8). Forecast for the full run:
about 45% to meet the whole target (range 38 to 50%). Recommendation: go, on 978793e8, if a miss that reads "level
within noise, cheaper, as correct" is an acceptable public result. No further cheap check would move the odds much.**

## Recount

| figure | runner | recounted | |
|---|--:|--:|---|
| Tree, model, agent CLI | 978793e8 | same in all 10; version string no longer `-dirty` | holds |
| First version green | 8 of 10 | 8 of 10 (trials 2 and 5 took 2) | holds |
| Mean versions to green | 1.20 | 1.20 | holds |
| Correct on hidden cases | 9 of 10 | 9 of 10 (trial 10 fails `overflow-min`, 24 of 25) | holds |
| Builds that rewrote the source | 8 | 8, in 7 trials | holds |
| Unaided first drafts green | 2 of 10 | **3 of 10** (trials 6, 7, 8; in 8 the rewrite came after green) | small slip |
| Spend | $1.35 | $1.3455 | holds |

For scale: paid agents on `calc` were 3 of 12 green first time on the old tree; the same old drafts rebuilt on main were
8 of 12; C was 10 of 12.

## What the trials show

- **The two misses are new causes, as expected.** Trial 2: `list.get(i)` does not exist (one compile error, one fix).
  Trial 5: the agent's own logic (its marker `n` for negation clashed with a variable named `n`). Neither is one of
  the three #1388 fixes. That fits the forecast's assumption that a new parser task fails about one draft in four.
- **The wrong program (trial 10) is the agent's logic**, not the compiler: the smallest value `% -1` should report
  overflow. The card warns about exactly this. C also produced wrong `calc` programs in paid runs (1 to 2 of 12).
- **One automatic fix changes meaning.** In 4 of 10 trials (3, 5, 8, 10) the agent wrote `trim_start(' ')` to strip
  spaces only, and the build rewrote it to `trim_start()`, which also strips tabs. All four agents noticed with their
  own tab test and wrote a loop. It cost no counted version, and no wrong program here, but it is the same "spaces
  only" need seen in `tally` trials 3 and 5. A sealed task where tabs matter and the agent does not test them would
  give a clean-but-wrong program. I would not change the compiler for it now: making it an error costs a version in
  4 of 10 drafts, and a new `trim_start(c)` is a feature that moves the frozen commit. Record it for after the run.
- Versions checked in total: 2.4 a trial (every agent but two kept editing after green). Same pattern as the pilot.
- Cost $0.135 a trial, as the pilot's parser task.

## Forecast

`sim.py` with the parser task's failure rate updated by 2 misses in 10 (3,000 runs, two seeds):

| | after fixes, before this check | now |
|---|--:|--:|
| Held out not "lost" | 64% | 69% |
| No class lost | 53% | 58% |
| Pooled upper bound under +0.10 | 62% | 67% |
| As correct, pooled and per class | 89% | 90% |
| **All criteria** | about 41% | **about 45%** |

It does not reach the 53% column, which needed parsers at about 90% green. Expected cost $55 to $58; the $78 cap fits
in the $90 left.

## Go / no-go

**Go**, with these conditions, all already planned:
1. Frozen run commit is 978793e8 exactly (the tree this check and the 570-program replay ran on). Nothing else merges.
2. Mac, Linux and Windows gates green on that commit; task check and `DRY_ONLY` green; first paid step is the
   two-trial `STOP_AFTER_FIRST`.
3. Nothing else builds AIL on the Mac during the run.
4. Kaleb's typed OK in the runner thread, having read the real API balance.

What to expect: the most likely single outcome is still a narrow miss (every class tied, pooled bound a little over
+0.10, or the held-out class lost on the sealed parser task). Cheaper and as correct are very likely to pass.

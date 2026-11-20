# Final paid run: independent review

2026-11-19. Frozen commit 978793e8, 464 trials, $54.81. Read-only: recounts from `final-run-trials-metrics.jsonl`,
the 303 non-sealed transcripts, and the 160 sealed transcripts read on the Mac (only counts and compiler messages
left the Mac; sealed tasks are called sealed1 to sealed4 here). No builds, no paid calls.

## Short version

1. **The result is good, and the verdict is still correctly NOT MET.** AIL was more correct (232/232 against 228/231),
   25% cheaper, level on two of three classes, and behind on tries only on the held-out tasks.
2. **Editing after green did not cost AIL the verdict.** The tries figure already stops counting at the first green
   test. C agents edited after green more often than AIL agents did (30 trials against 23). So "if they had stopped
   at first green" leaves tries exactly where they are and makes both arms about 4 to 5% cheaper.
3. **What did cost the verdict: 32 AIL first drafts that did not compile**, against 4 for C. Almost all are a guessed
   name or form the agent had never seen. Ten of them are one need: printing an integer padded with zeros.
4. **Estimate:** without those ten padding misses alone, the target would have been met, narrowly. With no
   unfamiliarity misses at all, AIL would have beaten C in every class. Both are estimates, not results.

## 1. The numbers hold

Recounted from the per-trial file; all match the report (my interval ends differ by 0.01 because of row order).

| class | AIL first draft green | C first draft green | AIL mean tries | C mean tries | 95% interval of the gap | call |
|---|--:|--:|--:|--:|--:|---|
| from scratch | 63/72 | 65/72 | 1.14 | 1.11 | -0.10 to +0.15 | tied |
| change | 73/80 | 74/79 | 1.09 | 1.06 | -0.06 to +0.10 | tied |
| held out | 63/80 | 75/80 | 1.23 | 1.06 | +0.05 to +0.28 | lost |
| pooled | 199/232 | 214/231 | 1.15 | 1.08 | +0.01 to +0.13 | bound over +0.10 |

Things in AIL's favour that the verdict line understates:

- **Correctness.** AIL passed every hidden case in every trial. C failed 3 trials.
- **Logic.** Only 1 AIL version failed the visible tests, against 14 C versions. When AIL code compiled, it was
  nearly always right. C's misses were mostly logic or spec misreadings, which no card or compiler help can fix.
- **Cost.** $0.101 against $0.135 a trial, and still cheaper with the card read taken out ($0.077 against $0.096).
  AIL agents wrote 25% fewer output tokens.
- **No trial hit a cap, and no AIL trial needed more than three versions.**

Things against, said plainly:

- 49 AIL builds repaired the draft silently and counted as green first drafts. That is the language working as
  designed, but unaided first drafts were 150/232, not 199/232. With a repair counted as a try the gap is
  +0.20 to +0.36.
- The held-out loss is real and not noise: the interval is clear of zero, and it is the class that best predicts
  tasks nobody has tuned for.

## 2. Why agents kept going after green

They did, in both languages, and for good reasons. Green means 4 to 12 visible cases pass; the agent knows hidden
cases exist.

| | AIL | C |
|---|--:|--:|
| trials that did anything after first green (mostly hand tests) | 96/232 | 72/231 |
| trials that changed the source after first green | 23/232 | 30/231 |

What the 23 AIL post-green edits were (read from the transcripts):

- **7 removed an unused variable** the build warned about (`expr.bind.14`). C agents did the same for clang warnings.
- **About 9 fixed a real bug found by hand-testing the spec's edge cases.** On sealed1, four agents found their
  program crashed on one malformed line and fixed it. Those trials passed the hidden cases; stopped at first green
  they very likely would not have.
- **The rest were tidying** (dead code, a comment's grammar).

So the behaviour is diligence, not confusion, and it is part of why AIL scored 232/232. Training data would not
remove it and should not. The unused-variable case is the one avoidable round: the warning already prints its fix.

## 3. Estimates

All of this section is an estimate from this run's data. None of it was run.

### 3a. If every agent had stopped at first green

Tries: unchanged, because the measure already stops there. Cost, with the calls between first green and the closing
message removed:

| class | AIL actual | AIL stopped | C actual | C stopped |
|---|--:|--:|--:|--:|
| from scratch | $0.097 | $0.092 | $0.138 | $0.132 |
| change | $0.103 | $0.099 | $0.132 | $0.127 |
| held out | $0.103 | $0.098 | $0.136 | $0.132 |
| pooled | $0.101 | $0.097 | $0.135 | $0.130 |

Verdict: still NOT MET, for the same two lines. Correctness would probably drop a little in both arms.

### 3b. If the unfamiliarity misses had not happened

This is the estimate that answers the training-data question. Causes of the 33 AIL trials that were not green first
time:

| cause | trials | where |
|---|--:|---|
| zero-padded integer: `n.pad_left(2, '0')`, or declaring a helper method on `int` | 10 | 6 held out, 4 stock |
| other guessed std names (`char.to_int`, `list.get`, `to_list`, BigInt names) | 8 | 4 held out, 4 ledger/stock |
| optional and error typing (`if` branches `T` and `T?`, `?` placement, `! str`) | 6 | all held out |
| one-line `if` in a scripted edit, module and local name clashes | 6 | change tasks |
| other (destructuring, tuple argument) | 2 | held out |
| logic | 1 | stock |

| scenario | held out | pooled gap | target |
|---|---|---|---|
| actual | 1.23 against 1.06, lost | +0.01 to +0.13 | NOT MET |
| padding misses gone (8 trials where it was the only error) | 1.16 against 1.06, tied (interval +0.00 to +0.20) | -0.02 to +0.10 | met, on the line |
| padding and `char.to_int` gone (10 trials) | 1.14 against 1.06, tied | -0.03 to +0.09 | met |
| half of the 32 compile misses gone, chosen at random | tied | upper bound about +0.05 | met in 200 of 200 draws |
| none of the compile misses (ceiling) | 1.00 against 1.06, won | -0.11 to -0.04 | met, AIL wins every class |

Read the ceiling as a ceiling. A model trained on AIL would still make some slips, as it does in C (4 C drafts did
not compile).

## 4. On "training data should fix that"

Agree on direction, with two cautions.

- The misses are exactly the kind training data fixes: wrong guesses at names and forms. The part training data does
  not fix, logic, is where AIL was already ahead (1 failed-test version against 14).
- Training data is slow and outside the project's control. The nearer lever is the compiler. For the padding miss
  it already printed the exact answer (`"{x:02}"`) in the help line and then failed the build anyway.
- Caution: every run so far has surfaced new guessed names after the last ones were fixed (pilot, calc check, now
  this). Fixing these ten and re-measuring on the same tasks would flatter AIL. The held-out gap is the honest
  measure of the long tail, and only new sealed tasks can show it closed.

## 5. What I would do next (no paid run needed)

1. Make the zero-padded integer forms work or repair themselves: `int.pad_left(w, c)` and a user helper on `int`.
   Largest single cause, 10 of 33.
2. Certain fixes for `char.to_int()` in the contexts that missed, `list.get(i)`, and `xs.to_list()` on a list.
3. Card lines for mixing `T` and `T?` in `if` branches and for `x[i] else`.
4. Public wording that this run supports: "as correct as C or better, cheaper, level with C on familiar task
   shapes, about one extra try in six on unseen tasks, all from names the model has never seen."

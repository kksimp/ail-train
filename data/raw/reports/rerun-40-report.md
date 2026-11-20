# Rerun report (frozen tree 767759a3784f2318b7140c40ed980e04c6757ce9, the agent model, agent CLI 2.1.318)

**Status: stopped at the plan's stage 10 ("lost") after round 10, at Kaleb's decision (2026-11-20).** 160 of the 312 plan rows ran: 80 ail-plain and 80 C trials on the 8 fresh tasks (sealed5 to sealed12; sealed12 is the validation task, reported apart). Spent $22.44 of the $38 cap. The remaining 152 ail-plain-only rows on the practised tasks were not run. Sealed task ids replace the real names throughout.

**Why sealed6's rows are a redo:** the first sealed6 rows (rounds 1 to 5) were 0 of 5 correct for both arms, which pointed at the task. The task was fixed (oracle, C and AIL follow the spec on token length, a spec sentence on the first word, unset before overflow, 94 regenerated cases) and rounds 1 to 5 were run again on the fixed task. The old rows are kept aside and not counted; their cost stays in the ledger.

**Note from Kaleb (his expectation, not a measurement):** we expect ail-plain to get much better once models pick up AIL. In this run the agents meet the language for the first time and learn it only from the docs they read before writing (about 29 KB for ail-plain, about 48 KB for C). Read the "lost" call below as a first-contact result, not a ceiling. What the data shows: correctness is level (78/80 against 79/80), ail-plain is about 20% cheaper per trial ($0.114 against $0.144), and the gap is in first drafts (56/80 against 70/80 first-version correct).

---

Not run: 11 task(s) have no scored trial, so their classes are not in the tables or the verdict, which is partial.

Primary measure: iterations to working code (fewer is better).

| class | arm | trials | correct | first version green | mean versions, all trials | mean versions to green (correct only) | mean fix rounds (correct) | builds that rewrote src | scratch compiles per trial | DOCS KB before first write (median) | vs c: 95% interval of the difference | call |
|---|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|---|
| held out | ail-plain | 80 | 78/80 | 56/80 | 1.35 | 1.33 | 0.32 | 25 | 0.00 | 29.9 | +0.07 to +0.38 | lost |
| held out | c | 80 | 79/80 | 70/80 | 1.12 | 1.11 | 0.11 | 0 | 0.00 | 47.9 | - | - |

A pilot makes no call: its cells are too small; the column is for the full run.

Pooled over all classes (ail-plain against c, bootstrap resampled within class): 80 and 80 trials; mean versions 1.35 against 1.12; 95% interval of the difference +0.07 to +0.38; correct 78/80 against 79/80, 95% interval of the difference in share -0.06 to +0.03; cost per trial $0.114 against $0.144.

Target of the final run (level on tries, cheaper, not shown to be less correct): **NOT MET**

- no class lost: NO
- pooled upper bound under +0.10: NO
- correct share not shown to be lower, pooled (95% interval of the difference -0.06 to +0.03; includes zero or is above it): yes
- correct share not shown to be lower in any class: yes
- cost per trial lower: yes

Secondary figures (not part of the verdict). Versions: the verdict's count, then with a build that rewrote the source counted as one more version. Cost per trial: total, then without the DOCS read, estimated as total minus DOCS tokens (bytes / 4) x (cache-write price + cache-read price x (turns - 1)), never below the output cost.

| class | arm | trials | mean versions | mean versions, rewrite counted | cost per trial USD | cost per trial without the DOCS read |
|---|---|--:|--:|--:|--:|--:|
| held out | ail-plain | 80 | 1.35 | 1.65 | 0.114 | 0.090 |
| held out | c | 80 | 1.12 | 1.12 | 0.144 | 0.106 |
| all classes | ail-plain | 80 | 1.35 | 1.65 | 0.114 | 0.090 |
| all classes | c | 80 | 1.12 | 1.12 | 0.144 | 0.106 |

Pooled gap in versions with a rewrite counted (95% interval, resampled within class): +0.32 to +0.74.

Held out without the validation task (it was in the library before the run): 70 and 70 trials; mean versions 1.39 against 1.14; 95% interval of the difference +0.07 to +0.41; call: lost (versions only).

| task | arm | trials | correct | stopped by a cap | median cost USD | median out tokens | median fix rounds | median versions to green | median debug rounds (calls) | median min | interventions | first check clean | median toolchain tokens | median calls to green | used agent tools | median DOCS KB received | median USD cache write / read / output |
|---|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| sealed10 | ail-plain | 10 | 10/10 | 0 | 0.10 | 3184 | 0.0 | 1.0 | 0.0 | 0.5 | 0 | 4/5 | 7.2 | 1.5 | 0/10 | 29.0 | 0.056 / 0.013 / 0.032 |
| sealed10 | c | 10 | 10/10 | 0 | 0.12 | 3486 | 0.0 | 1.0 | 0.0 | 0.5 | 0 | 0/0 | 7.2 | 1.0 | 0/10 | 46.9 | 0.077 / 0.013 / 0.035 |
| sealed8 | ail-plain | 10 | 10/10 | 0 | 0.12 | 4008 | 0.0 | 1.0 | 0.0 | 0.5 | 0 | 4/8 | 10.8 | 2.0 | 0/10 | 30.3 | 0.058 / 0.018 / 0.040 |
| sealed8 | c | 10 | 10/10 | 0 | 0.15 | 5292 | 0.0 | 1.0 | 0.0 | 0.7 | 0 | 8/8 | 7.2 | 2.0 | 0/10 | 47.9 | 0.081 / 0.014 / 0.053 |
| sealed9 | ail-plain | 10 | 9/10 | 0 | 0.10 | 2654 | 0.0 | 1.0 | 0.0 | 0.4 | 0 | 4/6 | 7.2 | 2.0 | 0/10 | 28.9 | 0.055 / 0.014 / 0.027 |
| sealed9 | c | 10 | 10/10 | 0 | 0.11 | 2747 | 0.0 | 1.0 | 0.0 | 0.4 | 0 | 1/1 | 7.2 | 1.0 | 0/10 | 46.6 | 0.074 / 0.012 / 0.027 |
| sealed7 | ail-plain | 10 | 10/10 | 0 | 0.09 | 2356 | 0.0 | 1.0 | 0.0 | 0.3 | 0 | 5/8 | 7.2 | 2.0 | 0/10 | 29.4 | 0.054 / 0.011 / 0.024 |
| sealed7 | c | 10 | 10/10 | 0 | 0.13 | 3870 | 0.0 | 1.0 | 0.0 | 0.5 | 0 | 6/6 | 7.2 | 2.0 | 0/10 | 47.1 | 0.078 / 0.013 / 0.039 |
| sealed5 | ail-plain | 10 | 9/10 | 0 | 0.17 | 7194 | 0.5 | 1.5 | 0.5 | 0.9 | 0 | 1/6 | 1079.8 | 3.5 | 1/10 | 31.0 | 0.073 / 0.023 / 0.072 |
| sealed5 | c | 10 | 10/10 | 0 | 0.18 | 7258 | 0.0 | 1.0 | 0.0 | 0.9 | 0 | 6/6 | 7.2 | 2.0 | 0/10 | 48.7 | 0.088 / 0.020 / 0.073 |
| sealed12 | ail-plain | 10 | 10/10 | 0 | 0.08 | 2079 | 0.0 | 1.0 | 0.0 | 0.3 | 0 | 6/7 | 7.2 | 2.0 | 0/10 | 28.2 | 0.052 / 0.011 / 0.021 |
| sealed12 | c | 10 | 10/10 | 0 | 0.11 | 2573 | 0.0 | 1.0 | 0.0 | 0.4 | 0 | 0/0 | 7.2 | 1.0 | 0/10 | 45.8 | 0.073 / 0.013 / 0.026 |
| sealed11 | ail-plain | 10 | 10/10 | 0 | 0.10 | 3371 | 0.0 | 1.0 | 0.0 | 0.5 | 0 | 6/8 | 39.4 | 2.0 | 0/10 | 30.3 | 0.057 / 0.014 / 0.034 |
| sealed11 | c | 10 | 10/10 | 0 | 0.14 | 4850 | 0.0 | 1.0 | 0.0 | 0.6 | 0 | 8/8 | 7.2 | 2.0 | 0/10 | 47.9 | 0.080 / 0.013 / 0.049 |
| sealed6 | ail-plain | 10 | 10/10 | 0 | 0.15 | 6692 | 1.0 | 2.0 | 1.0 | 0.8 | 0 | 4/7 | 77.2 | 2.5 | 0/10 | 31.6 | 0.068 / 0.019 / 0.067 |
| sealed6 | c | 10 | 9/10 | 0 | 0.20 | 8204 | 1.0 | 2.0 | 1.0 | 1.1 | 0 | 6/6 | 178.8 | 3.0 | 0/10 | 49.2 | 0.091 / 0.030 / 0.082 |
commit: 767759a3784f2318b7140c40ed980e04c6757ce9


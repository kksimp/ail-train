# E14 readiness: verdict of the five reviewers

2026-11-15. Synthesis by R1 from `R1` to `R5` `-round1.md` and `-round2.md` in this folder. Read and analysis
only: nothing was built, no model was called, no money was spent. Status: final; all five round-2 files are folded in. Evidence is the published E13 archive (480
trials, transcripts and token records), the S17 replay, and the tree at PR #1310 (cd45500f).

## 1. Verdict

1. **Plain AIL 0.2 will probably not beat C on the from-scratch tasks.** Reviewer estimates of the chance that
   `ail-plain` is cheaper than `c` there: 0.10 to 0.20. On change tasks we expect a tie. On the new till tasks
   there is no data; the lean is even to slightly AIL.
2. **The from-scratch headline will be decided by the harness, not by 0.2.** In E13 no C trial read its
   reference card (0 of 39 from scratch; section 3.1). E14 splits the cards and tells every arm to read each
   part. If the C agent obeys, C gets about $0.04 dearer and plain AIL lands within noise of it. If it does
   not, plain AIL loses by 40 to 70%. Either result says little about the language.
3. **We found one new way for AIL to lose on correctness**, which E13 did not have: the new card's first
   example reads lines with `lines()`, which silently drops `\r`, and hidden cases in depgraph and the stock
   family require a `\r` line to be rejected (3.2). One card line fixes it.
4. **Do not run the $10 pilot as written.** Unanimous. Its two arms (`ail-plain`, `c`) have only two possible outcomes,
   both already predicted, and it leaves out the one AIL arm that can win. Apply the free fixes in section 5,
   settle four decisions (section 6), and run the reshaped pilot (section 5.3) for the same money.
5. **What 0.2 did achieve.** Writing the three programs from the new card alone needed no lookup for arguments,
   stderr, exit codes, `never`, one-line `elif`, map access or sorting. Expect from-scratch turns of 8 to 10
   against 15.3 in E13, and lookups of 3 to 5 against 7 to 9. The gap that remains is mostly the price of
   reading a 16,000-token card that a C agent does not need.

6. **Even a clean cost win would not show what the benchmark was built to show** (R5, R2). Correctness is
   saturated on these tasks and cost is mostly documentation, so a win would show that a card can be made
   cheap, not that AIL helps agents engineer software. Tasks whose spec demands what C makes hard (unbounded
   input, arithmetic past 64 bits, nested data), held out from tuning, are the route to that claim.

## 2. Predicted outcome per task, `ail-plain` against `c`

Mean cost per trial. "C skips" is C as it behaved in E13; "C reads" is C obeying the new note. Ranges span the
reviewers. Prices (exact fit to E13): cache write $2.50, cache read $0.10, output $10 per million tokens.

| Task | E13 plain / C | E14 plain | E14 C skips / reads | E14 core card | Predicted call |
|---|---|---|---|---|---|
| ledger | $0.175 / $0.085 | $0.12 to $0.155 | $0.085 / $0.115 to $0.134 | $0.105 to $0.15 | C; tie only if C reads. AIL's worst task (`T ! str`, BigInt path) |
| depgraph | $0.145 / $0.069 | $0.10 to $0.13 | $0.069 / $0.10 to $0.117 | $0.08 to $0.10 | C; tie if C reads. AIL correctness at risk (`\r`) |
| stock | $0.149 / $0.073 | $0.10 to $0.13 | $0.073 / $0.105 to $0.121 | $0.08 to $0.105 | C; tie if C reads. AIL correctness at risk (`\r`) |
| ledger-fix | $0.052 / $0.053 | tie | | | tie |
| stock-bugfix | $0.053 / $0.055 | tie | | | tie |
| stock-decimal | $0.075 / $0.063 | C by a little | | | tie or C narrowly |
| stock-locations | $0.114 / $0.137 | AIL | | | AIL (the C change is twice the output) |
| stock-refactor | $0.114 / $0.075 | C, by less than E13 | | | C narrowly (modules; the card split is broken here, 3.3) |
| till-bugfix, till-returns, till-rename | none | $0.14 to $0.20 | $0.15 to $0.22 | | unknown; AIL code is 30% smaller, modules are AIL's weak spot |

Other measures: turns and fix rounds stay higher for AIL than for C on from-scratch tasks in every scenario.
Success ties at 11 to 12 of 12 if the `\r` line goes on the card; without it reviewers expect AIL at 6 to 11
of 12 on depgraph and stock. The plain arm's floor (card read once, clean first draft, 6 turns) is $0.105 to
$0.113; C without its card averages $0.076. The core card's floor is about $0.06 to $0.08.

Chances, pooled: plain below C from scratch 0.15; core card below C from scratch 0.45 to 0.6; plain below C on
the all-task mean 0.3 to 0.4; best AIL arm below C on all tasks about 0.5.

## 3. What we missed, ranked

1. **C never read its card in E13, and E14 changes that.** (R1, R4, R5 independently; R3 concurs; corrects
   R2 A3.) Card bytes actually received per trial, all 480 transcripts: from scratch, `c` 0 of 39 trials got
   20 KB or more, `rust` 36 of 37, `ail-plain` 39 of 39. The C card was 31.3 KB, just over the agent's 30 KB
   output cut; the Rust card 29.4 KB, just under. So E13 compared AIL plus a card with C plus nothing, and Rust
   ($0.096) was the like-for-like baseline. E13 and E14 C cells are not comparable, and an E14 "win" would be
   credited to 0.2 when the docs note produced it. `cat DOCS/*`, the usual first read, still exceeds the cut
   with the split parts (38 KB), so whether C reads is close to a coin flip.
2. **`s.lines()` and `io.read_line()` drop `\r`; the card does not say so and now models them.** (R1; ranked
   first by R3, R4 and R5 for their own lenses.) depgraph `crlf` and `strict-fields` in stock and its four
   change tasks are hidden cases with no visible twin. In E13, 73 of 75 AIL solutions on those tasks used
   `split("\n")`; the two that used `read_line` both failed exactly that case.
3. **The tasks were tuned on, and there is no held-out from-scratch task.** (R2 A1, R5.) Every 0.2 change was
   chosen from E13 transcripts of the same eight tasks. The till tasks are change tasks, where E13 was already
   level. A win on these tasks alone would not be believed, and the pilot followed by more fixes is a second
   tuning pass.
4. **"Beats C" has no written definition.** (R2, R3, R4, R5.) With 11 tasks, 5 arms and about 8 measures, some
   cell will favour AIL by chance.
5. **The card is now the largest cost, and it grew 30% for 0.2** (29.4 KB to 38.3 KB, about 12.8k to 16.7k
   tokens; the core card doubled to 8.8 KB). (R4, R5.) That cancels about 40% of what the 0.2 fixes save. Only
   the core-card arm has a floor near C's, and it is not in the pilot.
6. **The AIL card alone is split inside a code block.** (R3, R5; confirmed by replaying `split_doc`.) Part 1
   ends on an open fence in the Modules example at the comment `# src/store/store.ail`. The C and Rust cards
   split at headings. It hits stock-refactor and the till tasks.
7. **Hidden cases and solutions are reachable from the workspace.** (R2 A4.) `./test` and the `ail` shim hold
   the harness path. In the depgraph transcripts four trials looked around it and none opened a case; the arm
   that forages is AIL. One trial that reads `solution/ail/` voids a run. There is no audit.
8. **Value semantics give wrong answers without a diagnostic.** (R1 3.3, R5.) `mut it := m.get(k) else ...`,
   change `it`, never store it back: compiles, wrong totals. Also `mut` parameters and copies are documented
   after the card's "read to here" line (R1 3.2).
9. **The BigInt path is advertised but incomplete on the card.** (R1 3.4.) `m[k] += big` on a missing key and
   zero-padded formatting of a BigInt are unverified; no hidden case needs more than 64 bits, yet "sums may be
   large" plus the card's BigInt line will send AIL agents that way.
10. **Measurement asymmetries.** Fix rounds are logged only through the `ail` shim, including scratch probes
    (R2 B1, R3). `./test` hides compile errors behind a second call (R3). The S17 probe tally printed "0 FAIL"
    above a FAIL line; the failing probe is a wrapper artifact, but it shows that `qty := qty(s)` followed by a
    second call of `qty` in the same block is an error agents will meet (R5, R1).
11. **Budget.** If every arm reads its card on every task, the 660-trial run costs $90 to $110 against the
    $100 cap (R4).
12. **Not a benchmark question, but raised:** correctness is saturated, so cost is the only thing measured, and
    no task exercises what AIL is for (overflow, memory safety, large inputs). And 0.2 moved the language toward
    one model's guesses (R5). Further "accept the habit" proposals (`T ! str`, bare `eprint`, `else if`) should
    be judged against ADR 1077's first criterion, not against E14.

## 4. Where the reviewers still differ

- Chance that C reads its split card: 0.5 (R5) to 0.6 (R4). Agreed that it should be set by policy, not left
  to chance.
- A `\r` line in a visible case (R3 proposed, R2 objects): it would move a hidden case into view because one
  arm fails it, which ADR 0916's amendment of 2026-11-15b already rejected for the argument-rule cases. The
  verdict sides with R2: the card line only. If AIL still fails `crlf`, that is a finding to report.
- Held-out tasks: in the full run only (R4), or one in the pilot too because the pilot's question is "what
  else is wrong" (R1, R2). R2: a task used in the pilot is no longer held out, so write three and spend one.
- "Look up, never guess": reverse it for names the checker corrects (R3, R5), or wait for the pilot's share of
  whole-file rewrites (R4, R1).
- Primary measure: settled in round 2 on from-scratch tasks, with held-out from-scratch tasks as a separate
  primary table (R2 accepts R4's point), change tasks and till secondary.
- Core card as the headline arm: yes on cost (R3, R4, R5); R4 notes it has the most fix rounds, so name the
  measure first. R2: choosing the arm from E13's results is post hoc selection unless it is justified
  otherwise ("it is what `ail new` gives a user"), disclosed as chosen after E13, and every arm is reported
  beside it with the same prominence.

## 5. Concrete fixes

### 5.1 Free, before any paid trial

Card (one docs PR; skips the gates):
1. Beside the stdin sentence on both cards: "`s.lines()` and `io.read_line()` drop a `\r` before the line end;
   to see it, split with `s.split("\n")`."
2. Move the `mut` parameter lines (`fn bump(mut p Point)`, `bump(mut q)`) before Modules, with a Habits line.
3. Maps: "`m[k].qty += 1` changes the entry in place; `it := m[k]` is a copy, store it back with `m[k] = it`."
4. Correct the format-spec sentence to the spec's grammar (it denies `{n:08}`, which the line above uses).
5. Small: `m.keys().sorted()` spelled out, byte order of `str`, parentheses for `else` inside an expression,
   `to_int()` strictness, "hides the function to the end of the block" with an example.
6. Probe on the Mac (seconds, no model): `m[k] += bigint.from_int(n)` on a missing key, `"{b:0>2}"` on a
   BigInt, the text of expr.call.1 when a local hides a function, and that `ail build` prints `fix: write`
   as `ail check` does. Put the working BigInt money form on the card.

Harness (neutral, every arm):
7. `split_doc`: never cut inside a fence.
8. (Withdrawn: a visible `\r` case; see section 4.)
9. `./test` prints the build output when the build fails.
10. Record per trial the DOCS bytes received and cost by token class; report both.
11. A transcript audit in `report` listing any path outside the workspace; void a trial that read `tasks/` or
    another trial. Scan the E13 archive with it, and stop printing the harness path in `./test`. Before the
    pilot, not only the counted run: 5 of 36 AIL depgraph trials left the workspace, no C or Rust trial did.
12. Count fix rounds only from `./build`, `./test` and calls on `src/`, or demote the measure.
13. Alternate arm order between trials; pin the tree commit and record the agent CLI version.

Record (ADR 0916):
14. The win rule, written before the run: metric, arm and the reason for the arm. The pilot makes no win or
    loss call at all (R2 withdraws the ratio rule for the reshaped pilot; at 3 trials a cell the pooled
    from-scratch ratio is good to about plus or minus 15 to 20%).
14a. Correct the E13 record: ADR 0916 says the output cut "cost 59 C trials a turn"; it removed C's card. The
    published E13 comparison was AIL with a card against C without one. Say so in the ADR and on the wiki
    page before E14 (the wiki edit is a public step and needs the designer's go-ahead).
14b. A table in the E14 report of every harness and task change since E13 (seed rule, spec wording, doc split,
    fence fix, `./test` output, prompt, card sizes, C card content, arm order, fix-round counting) and the
    arms each can affect. E13 to E14 comparisons only on cells whose conditions did not change.
14c. Report doc parity as tokens actually ingested per arm, not as the 5% card-size check.

### 5.2 Larger, most likely to change the result

15. Give the plain arm one DOCS file of at most 24 KB (the card through Modules plus the moved `mut` lines); the
    rest through `ail card TOPIC`. About $0.02 a trial, more than any 0.2 language change, and it removes the
    split. Doc parity then shrinks the C card back.
16. (Ranked with 5.1 by R2: without it there is no primary result to defend.) Three held-out from-scratch
    tasks, one spent in the pilot, written without sight of E13 transcripts, in other areas (for example one
    that prints braces or JSON, one small evaluator or grid), frozen before the pilot, reported separately.
17. A warning for a local copy of a map or list entry that is changed and never stored or read.

### 5.3 The pilot, reshaped (about the same 44 trials, under $10)

- ledger, depgraph, stock: `ail-plain`, `ail-core-card`, `c`, 3 trials each (27 trials).
- till-bugfix, till-returns, till-rename: `ail-plain`, `c`, 2 trials each (12 trials).
- stock-refactor: `ail-plain`, `ail-core-card`, `c`, 1 trial each (3 trials).
- One held-out from-scratch task, if ready: 3 arms, 2 trials (6 trials).
- Drop ledger-fix, stock-bugfix, stock-decimal, stock-locations from the pilot: flat in E13, no open question.
- Stop after the first C trial and read its card bytes. That one number selects the scenario.
- What it can show: a harness or 0.2 regression, till's cost, whether C reads, whether the `\r` and copy traps
  occur, and a coarse behind or ahead call. What it cannot: a per-task result, or any gap under about 30%.
  Pilot trials are not merged into the full run.

## 6. Decisions for the designer

1. **What "beat C" means.** Recommended: mean cost per correct trial on from-scratch tasks, one AIL arm named in
   advance, against C in its natural condition; change tasks, till and held-out tasks reported separately;
   turns and success secondary.
2. **Docs policy.** (a) Every arm's prompt says DOCS is a reference to consult as needed, and the report shows
   what each arm read (recommended by R1, R4, R5); or (b) keep "read each part" and add `c-nodocs` and
   `rust-nodocs` cells on from-scratch tasks (about $5). E13's C cells already are the no-docs condition.
3. **The headline AIL arm.** The core card (what `ail new` gives a user; floor near C's) or the full card
   (floor above C's mean). And whether the plain arm's DOCS drops to 24 KB (item 15).
4. **Held-out tasks** (item 16): yes or no, and whether one goes into the pilot.

A goal this benchmark can honestly support: with the core card, an agent writes a small command-line program
in AIL for about what C costs, and on existing AIL code it works at parity or ahead. "Plain AIL beats C from
scratch" is not reachable under a comparison a skeptic would accept, because a C agent needs no card.

## 7. Run the $10 pilot as-is?

**No.** Unanimous, five of five. Do items 1 to 14c first (docs and harness, no gates beyond the doc checks and a harness dry
run), take the four decisions, then run the pilot in 5.3.

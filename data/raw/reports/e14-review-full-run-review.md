# E14 full run: review

Date: 2026-11-17. Tree: main 511d5efa. 840 trials, $97.53. Source: the per-trial `metrics.json`,
`.bench/runs.jsonl`, build and test outputs, final sources and transcripts in `~/ail-e14/results` on the Mac,
plus the four reports in the library root. Analysis only: nothing was built or run, and no paid trial was started.
Hidden-case contents are not reproduced here.

## Short answers

1. **The calculator result is not a harness bug.** All 12 tools-arm programs are wrong in the same way, and the
   cause is in AIL's card: `checked_rem`. See section 1.
2. **"All arms tied C on unseen tasks" is too kind to AIL.** The report averages versions over correct trials
   only, so the tools arm's 12 calculator trials (its hardest) dropped out. Over all trials AIL needed about 1.4
   to 1.5 versions against 1.11 for C. The whole gap is the calculator task, and one 0.2 feature causes most of it.
3. **Three causes explain 62 of the 138 failed AIL versions**, and each has a small fix. See section 3.
4. **The headline arm should stay the plain arm.** It gave a correct final program in all 162 of its scored
   trials (C 162 of 163, Rust 161 of 164). The core card is cheaper but was wrong 5 times of 12 on the
   calculator. See section 5.
5. **The 19 voided trials do not bias any arm.** See section 4.

## 1. Why the tools arm failed every calculator trial

Every failing trial failed one hidden case, the one about the smallest 64-bit value. The task says that the
smallest value `%` -1 is an overflow error. AIL defines `a % -1` as 0 for every `a` (`expr.arith.5`, ADR 0115),
and `checked_rem` follows it, so `checked_rem` gives 0 there and not `none` (`type.num.12` says so in the spec).
The card's line says only "`none` on overflow or zero divide".

| arm | DOCS it received | trials using `checked_rem` | of those, failed the case | trials not using it | of those, failed the case |
|---|---|--:|--:|--:|--:|
| ail-tools | whole card in two parts, 46 KB | 12 | 12 | 0 | - |
| ail-plain | front of the card (through Modules), 28 KB | 0 | - | 12 | 0 |
| ail-core-card | core card, 13.5 KB | 2 | 2 | 10 | 0 |

It is a perfect split: 14 of 14 programs that call `checked_rem` fail the case, 0 of 22 that do not.

- The two arms did **not** have the same guide. The plain arm gets only the front of the card; the `checked_*`
  line is in part 2, which only the tools arm receives. The two core-card trials found it with `ail ask`.
- The plain arm wrote the overflow tests by hand against a `MIN` constant and got them right.
- The task's own AIL solution avoids `checked_div` and `checked_rem` for this reason.
- So the trials are scored correctly. The agents trusted a card line that is incomplete.

Fix (docs only): add to the card's `int` line and to `ail explain`/`ail ask` that `checked_rem(-1)` is always 0,
and that a `MIN % -1` overflow needs its own test. Changing `checked_rem` itself would change ADR 0115, a
designer decision; I don't recommend it.

The other calculator failures are a task trap shared by every language (a line with leading spaces):
core card 4, Rust 2, C 1. One Rust trial failed the keywords case.

## 2. The numbers again, over all trials

The report's "mean versions to green (correct)" drops a trial whose final program fails a hidden case.
Versions to the first green visible run, over every trial:

| class | ail-plain | ail-tools | ail-core-card | c | rust |
|---|--:|--:|--:|--:|--:|
| from scratch (108 AIL trials) | 1.28 | 1.28 | 1.19 | 1.03 | 1.00 |
| change, voids included | 1.21 | 1.21 | 1.17 | 1.10 | 1.22 |
| held out, all trials | 1.42 | 1.50 | 1.44 | 1.11 | 1.00 |
| held out, as reported | 1.42 | 1.08 | 1.29 | 1.11 | 1.00 |

Held out by task (all trials):

| task | ail-plain | ail-tools | ail-core-card | c | rust |
|---|--:|--:|--:|--:|--:|
| calc | 2.25 | 2.33 | 2.08 | 1.08 | 1.00 |
| invjson | 1.00 | 1.00 | 1.17 | 1.25 | 1.00 |
| maze | 1.00 | 1.17 | 1.08 | 1.00 | 1.00 |

`invjson` was the pilot's losing task; after the brace fixes AIL now beats C on it. `maze` is level. The
calculator is the whole held-out gap.

Mean cost per from-scratch trial: core card $0.082, plain $0.100, Rust $0.116, tools $0.124, C $0.142.

## 3. Root causes of the failed AIL versions

A failed version is a distinct `src/` state whose build or test failed. All three AIL arms, 372 scored trials
plus voids: 138 failed versions.

| # | cause | kind | from scratch | change | held out | total |
|---|---|---|--:|--:|--:|--:|
| 1 | `T ! str` gaps | language gap (0.2 feature) + auto-fix gap | 0 | 0 | 30 | 30 |
| 2 | Logic error, test failed | agent (language-neutral, see note) | 8 | 11 | 4 | 23 |
| 3 | `mut tot := {}` then a store reported as "a list index must be `int`, found `str`" | compiler slip | 0 | 18 | 0 | 18 |
| 4 | Misplaced or misindented text from a scripted edit | agent editing habit | 0 | 17 | 0 | 17 |
| 5 | `for i, l in xs` | auto-fix gap | 0 | 5 | 0 | 5 |
| 6 | `n.pad_left(2, '0')` on an `int` | auto-fix gap | 5 | 0 | 0 | 5 |
| 7 | Missing `use` of a module that exists, or a moved item | auto-fix gap | 0 | 5 | 0 | 5 |
| 8 | `r := fallible()` then `if t := r ... else err` | diagnostics gap | 4 | 0 | 0 | 4 |
| 9 | `[[] for i in 0..n]` | diagnostics gap | 3 | 0 | 0 | 3 |
| 10 | `native.subset.1` after `ail check` passed (tuple sort key, BigInt where `int`, `int` to `any ToStr`) | compiler slip | 2 | 1 | 0 | 3 |
| 11 | `opt.map(\|x\| ...)` on an optional | card gap | 1 | 1 | 1 | 3 |
| 12 | `", ".join(xs)` | auto-fix gap (pilot fix 4, not landed) | 0 | 0 | 2 | 2 |
| 13 | BigInt and `int` mixed | card gap | 2 | 0 | 0 | 2 |
| 14 | Other, one each (precedence of `else`, `by:` with a function value, `int.MIN`, `trim_start(' ')`, read-only parameter, local hides module) | mixed | 2 | 5 | 11 | 18 |

No failed version is a harness fault.

### Cause 1: `T ! str` (30 versions, all on the calculator)

The calculator wants "do this or fail with a message" in every parser function. Agents wrote what 0.2 invites:

- `fn expr(mut self) ! str` for "no result, fails with text". It parses as a `str` result with inferred
  errors, which ADR 1129 lists as a known gap. The checker then says "must end with an expression of type
  `!str`" and "expected `!`, found `str`" on `return "syntax"`. Neither message names the gap.
- `fn run_line(...) str ! str`: `err.str.2`. Agents fell back to `int ! str` with a dummy value.
- A body ending in a bare `"syntax"` as the failure (11 versions). The rule needs `return`.
- `run_line(...) else err` as a statement on an `int ! str` call: `err.else.4`.

Fixes:
- **Auto-fix, certain:** in a `T ! str` function with `T` not `str`, a body-ending `str` expression becomes
  `return ...`. The type decides it, as ADR 1129 already argues. About 11 versions.
- **Diagnostics:** when a `! str` function has a bare `return`, ends in a statement or returns only text, say
  what `! str` means and show the working form. Today that form is an error type or a dummy result, which is
  the real problem.
- **Designer decision:** 0.2 has no spelling for "no result, fails with text". This is a hole in a new
  feature, not a request to copy another language. Options: (a) leave it and teach an error type in the card
  and the diagnostic; (b) give it a spelling. I recommend deciding before the tag, since 0.2 advertises
  `T ! str`; (a) is the cheap path and does not block the tag.

### Cause 3: `{}` and the list-index message (18 versions, one task)

`ledger-fix` seeds `mut tot := {}`. Every plain trial (12 of 12) and 6 tools trials changed the store to
`tot[key] = (tot.get(key) else bigint.from_int(0)) + ...`. The first use is now `tot.get(key)` inside the
right-hand side, the map's type is not fixed yet, and the checker reports a list index error on a map. The
agents fixed it in one round by naming the type, but the message sent them nowhere. The core-card arm rewrote
the declaration in the same edit and never saw it.

Fix: let the store on the left fix the type before the right-hand side is checked, or at least report
"the type of `{}` isn't known yet; write `Map[K, V]()`" with that as a certain fix.

This one message is why the headline arm "lost narrowly" on change tasks. Without those 12 versions the plain
arm's change mean is 1.09 against 1.11 for C; the tools arm's is 1.14.

### Cause 2: logic errors

From scratch AIL had 8 failed test versions in 108 trials; C had 1 in 36 and Rust 0. Four are the same case,
`ledger` "top N by absolute amount, ties in input order". AIL has no stable descending sort: the card says
descending is `xs.sorted().reversed()`, which reverses ties, and negating the key overflows on the smallest
value, so agents built sign tricks and got them wrong. A `sorted(by: ..., desc: true)` or a card how-to for
"largest first, ties in input order" would remove these. The rest (topological order direction twice,
quantity 0 twice) would happen in any language.

### Cause 4: scripted edits

On the larger change tasks agents patch with Python `replace` or `sed` on an anchor line such as
`    return BadLine`. The anchor matched a deeper line, and the inserted block landed at the wrong depth or
between a signature and its body. In an indentation language that is a syntax error; in C the same slip
compiles and shows up as a failed test (C had 9 failed test versions on change tasks, Rust 21 failed
compiles). I see no cheap compiler fix, and I would not count it against AIL more than against the others.

## 4. The 19 voided trials

By arm: ail-plain 6, C 5, Rust 4, ail-tools 3, ail-core-card 1. All on three change tasks (`till-returns` 7,
`stock-locations` 10, `stock-decimal` 2).

- Every voided trial ended correct. Their mean versions: plain 1.00, C 1.00, core 1.00, tools 1.33, Rust 1.25.
- With them counted the change-class means move by at most 0.014 (plain 1.222 to 1.208, C 1.110 to 1.104).
  No call changes.
- What they read: 13 ran `ls ../.bench` at the end of a `cat` of the sources, 5 read the start of
  `visible.jsonl`, which holds the same visible cases `./test` prints, and 1 (C) is a script whose flagged
  path the report cuts off. Hidden cases are not in the workspace, so none saw one. The rule is conservative, which is the right side to err on.
- One inconsistency for the harness: `stock` ail-tools 3 and ail-core-card 12 also read `.bench/visible.jsonl`
  (after a failed test, to see the failing case) and were not voided. The audit should treat both the same way.

## 5. Which arm should be the headline

Keep **ail-plain**.

- Correct final program: plain 162 of 162 scored trials; core card 162 of 167, all 5 misses on the calculator;
  tools 153 of 165, all 12 on the calculator.
- The core card's lead on versions from scratch (1.19 against 1.28) is 3 failed versions in 36 trials, inside
  the noise.
- The core card is clearly the cheapest (about 40% under C per trial). Report it as the low-cost arm.
- **Drop or rethink the tools arm.** No tools-arm trial used the agent tools (0 of 165), it costs $0.024 more
  per trial than plain for a card twice the size, and it did no better.

## 6. What to fix before tagging 0.2

Ranked by failed versions removed. None changes syntax.

| fix | kind | versions removed | size |
|---|---|--:|---|
| `{}` typed by a store whose right side reads the same map; or a clear message with a certain fix | compiler | 18 | small |
| `T ! str`: certain `return` auto-fix, and a diagnostic that names the no-result gap | auto-fix + diagnostics | about 20 of 30 | small |
| `for i, x in xs` to `xs.enumerate()` | certain auto-fix | 5 | small |
| `n.pad_left(w, c)` on an `int` to `"{n}".pad_left(w, c)` | certain auto-fix | 5 | small |
| Add `use M` when `M` is a module of the project | certain auto-fix | 3 to 5 | small |
| `r := f()` then `if t := r`: say "write `if t := f()`" | diagnostics | 4 | small |
| `[[] for ...]`: help shows `[List[int]() for ...]` | diagnostics | 3 | tiny |
| `", ".join(xs)` (pilot fix 4) | certain auto-fix | 2 | small |
| Card: `checked_rem(-1)` is 0; stable descending sort how-to; an optional has no `map` | card | section 1, and up to 7 | tiny |
| `native.subset.1` with no source line after a clean check | compiler | 3 | unknown, do after the tag |

Expected effect if the small ones land: from scratch about 1.25 to about 1.12 across the AIL arms (C 1.03), so
the gap halves but does not close; change tasks level with C; the calculator from about 2.2 to about 1.5.
These are projections from this run, not measurements.

## 7. Recommendation

- The run is sound. Do not rerun it to "fix" the calculator result; publish it as it is, with the all-trials
  table from section 2 in place of the correct-only one.
- Do not tag 511d5efa as 0.2 yet. Land the first two fixes and the card lines (a day of lane work, Mac gate),
  then tag. They remove 48 of the 138 failed versions and the one card line that made 14 programs wrong.
- Honest public wording for this run: AIL is the cheapest and the plain arm never shipped a wrong program,
  but it still needs more tries than C to reach working code from scratch.
- Report fix for the harness: average versions over all trials, and print correct-only beside it.
- A confirmation run after the fixes needs a paid run and Kaleb's OK; the calculator, `ledger-fix` and
  `ledger` for the three AIL arms and C would be about 144 trials, roughly $17.

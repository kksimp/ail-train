# Agentic coding test: ledger in AIL and Python

Builder: the API builder model; spec, hidden tests and analysis: the helper model (names in config.local).
AIL at the commit in .ail-version. 8 hidden cases, graded byte for byte.

## Numbers

|  | AIL | Python |
|---|---|---|
| Hidden cases passed | 8/8 | 8/8 |
| Public cases passed | 3/3 | 3/3 |
| How the build ended | finished | finished |
| Model turns | 11 | 3 |
| Tool calls | 14 | 4 |
| Compile or run attempts | 5 | 2 |
| Attempts that failed to compile / raised | 0 | 0 |
| Program lines | 166 | 117 |
| Program tokens (same tokenizer) | 1769 | 1435 |
| Wall time (min) | 1.2 | 0.5 |
| API cost (USD) | 0.25 | 0.11 |
| Builder output tokens (incl. thinking) | 6422 | 3382 |

AIL build read (category: count): {"ail docs": 4, "ail spec": 2}

Compiler rule IDs hit: {}

## Spend

- spec: $1.75 (2 calls)
- ail: $0.25 (12 calls)
- py: $0.11 (4 calls)
- judge: $0.26 (1 calls)
- total: $2.37 of the $15.00 cap

## Verdict

The AIL app worked: 8/8 hidden and 3/3 public cases, with no failed compiles and no runtime traps. Python matched it on correctness and was cheaper on every process measure: 3 turns against 11, $0.11 against $0.25, 0.5 against 1.2 minutes, and a program 19% smaller in tokens (1435 against 1769). This one run shows that a model new to AIL can write a correct small text-processing app from the docs on its first try; it cannot show AIL is better for agents, because neither language produced a bug to catch.

## What helped

- **A compact card was enough.** The build read three files (`llms.txt`, `language-card.md`, `04-types.md`) and never opened the examples or training data. It got I/O, maps, in-place `m[k].field += 1`, tuple-key stable sorts and `T?` binding from those.
- **Tuple sort keys.** `(kind_index(a.kind), 0 - a.balance, a.name)` gave the three-level sort on the first try, including the byte-order tiebreak.
- **The card's warning about copies.** The builder says "`it := m[k]` copies the entry" steered it to mutate `accts[k].balance` directly. That avoided a likely silent bug.
- **The auto-fixer.** `to_string` was rewritten to `to_str` with a rule ID and location, which saved an edit–check round.
- **`words()`.** It tokenises on whitespace runs with no empty pieces, so tab handling and blank lines came free.
- **Guesses that held.** `if`/`elif` as an expression and `elif amt := parse_amount(...)` both compiled without the builder having seen an example. That suggests the syntax is guessable.

## What did not help

- **Lookup overhead dominated the cost.** The first clean check came on turn 7; Python was finished in 3 turns. The builder says most of that went on method names and edge semantics it would simply know in Python. The 2.3x cost is a familiarity tax, not a language defect, but it is real.
- **The card names the `to_string` habit but not the correct name.** The builder learned `to_str` only from the fixer.
- **Undocumented edge semantics.** The docs the builder read do not say:
  - whether `pad_left`/`pad_right` truncate a string longer than the width;
  - whether `is_alpha`/`is_alnum` are ASCII-only or Unicode;
  - what `words()` counts as whitespace.
- **The padding gap was shipped untested.** The spec says wide values are "never truncated", and the builder finished without checking that. The hidden cases passed, but we don't know from this data whether any of them has an over-wide value.
- **Char-to-digit is clumsy.** `cs[i].to_str().to_int()?` and `"{a}{b}".to_int()?` are roundabout. With no regex in play, `parse_amount` runs to about 35 lines against Python's 8.
- **The telemetry disagrees with itself.** The harness lists no compiler rule IDs hit and no failed compiles, yet the compiler rewrote the file once under `[expr.name.1]`. Auto-fixed errors seem to be invisible in the rule counts, which hides the most common foreign-habit data.

## What would help more

1. **AIL docs: state the edge behaviour on the card.** One line each would do it:
   - `pad_left`/`pad_right` and width format specs never truncate;
   - `is_alpha`/`is_alnum`/`is_digit` are ASCII or Unicode;
   - the exact whitespace set for `words()`;
   - `to_str()` written next to the `to_string` habit.

   This would have removed the spec lookup and the one untested risk.
2. **AIL compiler/tools: a char-to-digit method.** Add `c.to_digit()` returning `int?`, or document it if it exists. If AIL has a pattern or regex facility, show it on the card; if not, consider a small validator helper for token formats.
3. **AIL compiler/tools: log auto-fixes in the harness rule counts.** Then `expr.name.1` hits can be measured across runs and fed back into docs and training data.
4. **ail-train data: line-oriented command interpreters.** They should show `words()` tokenising, `if`-expression dispatch, `elif x := opt()` chains, `Map[str, Struct]` updated in place, multi-key sorts with a descending key, and fixed-width tables. This is the shape of many benchmark apps, and the builder guessed at several of these.
5. **AIL docs/tools: an `ail ask how` entry for fixed-point money parsing without floats.** `ail explain` was never called, so the card has to carry this content or point to it.
6. **ail-train data: `to_str` in many contexts.** That should make small models stop writing `to_string` rather than lean on the fixer.

## Evidence for AIL being better for agents

**Errors caught before running.** There was one, and it was a method-name habit from other languages. That is an error AIL's unfamiliarity created, not a logic bug that a stricter language prevented. Python had no bugs at all. So this run has no case where AIL's checker caught something Python would have let through.

**Safety features that might matter.**
- `int?` forces the caller to handle a bad amount. The Python version handled `None` correctly anyway.
- Overflow trapping never comes into play: the 10^12 cap means it would take millions of posts to get near a 64-bit limit.
- Insertion-ordered maps and a stable sort are things Python has too.

**Local reasoning and readability.** The two programs are nearly the same shape: one dispatch chain with an error string. AIL's `elif amt := parse_amount(...)` is a little tidier than Python's nested `else: v = ...; if v is None`. The typed `Account` struct is clearer than Python's `[kind, balance, posts]` list with numeric indexes. That is a real but small readability gain, and it was the Python builder's choice to use a list rather than a dataclass.

**Tokens and cost.** These go against AIL: 23% more program tokens, 42% more lines, 1.9x the output tokens and 2.3x the cost.

**Reading it fairly.** The result is parity on correctness at higher cost, reached by a builder with far less AIL experience. That counts for learnability; it is not evidence that AIL is better. The task is also too easy to tell the languages apart, because Python got everything right in one shot.

**What would settle it.**
- 30 to 50 specs of graded difficulty, including ones where Python builds fail hidden cases today through `None` mishandling, mutation aliasing, integer or float slips, or unhandled input shapes.
- Several seeds per spec and language.
- Hidden suites that target each spec's edge clauses, such as over-wide columns here.
- Measures: hidden pass rate, bugs caught at check time against bugs that reach a run, and cost to green.
- A second phase where an agent modifies an existing program, which is where types and local reasoning should pay off.
- A repeat with a small model fine-tuned on AIL, to separate the familiarity tax from the language's own properties.

## Code review

**AIL**
- Correct against the spec as far as I can trace. The check order is right, including MOVE testing both accounts exist before `same account`.
- `parse_amount` enforces the 11-digit cap, the exact `.dd` form and the 10^12 bound, and `-0.00` comes out as 0.
- `text.split("\n")` leaves a trailing empty element. That is harmless because an empty line is skipped and line numbers are unaffected.
- Risks:
  - `words()` probably also splits on `\r`, `\v` and `\f`, and `is_alpha` may accept non-ASCII letters. Both fall outside the spec's ASCII input guarantee.
  - Padding behaviour for over-wide values is assumed, not verified.
- Idiom:
  - Sending REPORT to the final `else` is slightly fragile; an explicit `elif cmd == "REPORT"` would be safer.
  - The digit conversion via strings is awkward.
  - `0 - v` in place of unary minus looks over-cautious.

**Python**
- Correct. `fullmatch` regexes, splitting on space and tab only, and the separate 10^12 check are all deliberate and right.
- It collapses the two `unknown account` checks into one `or`, which is equivalent.
- Idiom issues:
  - an `err` closure is redefined on every loop iteration;
  - account records are positional lists (`accts[f][1]`), which is error-prone under later changes;
  - output is buffered and written once, which is fine here.
- The Python builder's self-report says it ran only one public case itself. The 3/3 figure comes from the harness, so its own testing was thinner than the AIL builder's.

## Builder's self-report: AIL

1. Result

I think the program works, but the testing has gaps. work/app.ail passes `ail check` with "6 functions, 0 warnings". All three public cases (worked_example, errors_and_close, sort_ties) give exactly the expected output. I also ran one 39-line edge-case input. It covered:
- leading and trailing tabs, and an indented comment
- every invalid amount the spec lists (`+5`, `.50`, `5.`, `5.5`, `1.234`, `1,000`, `-`, 12 whole digits)
- exactly 10^12 accepted, 10^12+1 rejected, `-0.00`, and leading zeros
- name length 12 versus 13, a leading digit, `$` in a name, and a kind with the wrong case (`Asset`)
- MOVE with the same account, an unknown account, a negative amount and a non-numeric amount
- CLOSE of an unknown account, CLOSE with the wrong argument count, and closing then reopening
- uppercase sorting before lowercase in a balance tie

Empty input printed `ok=0 errors=0`. Every result matched my reading of the spec.

The gap: I never tested a value wider than its column. My one attempt used a 22-character name, which fails as `bad name` before any report shows it, so it tested nothing. My code assumes `pad_right`/`pad_left` never truncate. I did not check that in the docs or by running it, and I called finish without closing that gap. Posts counts above 99999 and balances wider than 16 characters are also untested.

2. What helped

- **`run_ail card`** (the core card) was the most useful resource. Within one read I had `io.read_all()`, `split`, `chars()`, `m.get`/`contains`/`remove`, `m[k].field += 1` updating in place, the stable `sorted(by:)`, and the `T?` + `else` / `?` pattern. Its warning "`it := m[k]` copies the entry" made me write `accts[args[0]].balance += amt` directly instead of copying, changing and storing back.
- **docs/language-card.md lines 226–253.** These gave me `words()`, `pad_left(width, ' ')`/`pad_right`, and the line "a tuple key `(a, b)` orders by `a`, then `b`". The tuple key let me write the three-level sort as `(kind_index(a.kind), 0 - a.balance, a.name)` with no comparator. It worked on the first try, including the byte-order string tiebreak.
- **docs/spec/04-types.md, type.str.17.** It confirmed that `words()` splits on runs of whitespace and gives no empty pieces, so tab handling and blank lines came free.
- **The auto-fixer.** I wrote `cs[i].to_string()`. `check` rewrote it with "fixed work/app.ail:40:36: [expr.name.1] write `to_str`", and the file then compiled. Applying the fix and saying where was fine.
- Line 457 of the card lists the char predicates (`is_digit`, `is_alpha`, `is_alnum`). I found it with one grep.

I never looked at ail-train/data/extra or the examples; the card and spec were enough.

3. What did not help or misled you

- **`to_string`.** The core card lists `to_string()` among the habits that get auto-fixed, so it is a known trap. But the card never says the real name is `to_str` anywhere I read it. I only learned it from the fixer.
- **Missing details on padding and format specs.** The card says `s.pad_left(width, ' ')` but not what happens when the string is already longer than `width`. This spec, like many console-app specs, depends on that ("never truncated"). The same question applies to `{n:>6}` format specs.
- **`is_alpha` / `is_alnum`.** The card does not say whether these are ASCII-only or Unicode. For validating names that matters. ASCII-only input saved me here, but in general it would not.
- **`words()` and "whitespace".** The card mentions `words()` only in a long list and never says what counts as whitespace (tab? `\r`? `\v`?). I had to go to the spec to find out, and even type.str.17 just says "whitespace".
- Nothing actively misled me. No compile error confused me, because there was only the one auto-fixed error.

4. What would help more

- **Card:** state the truncation behaviour of `pad_left`/`pad_right`/`center` and of width format specs ("never truncates; a longer string is returned unchanged"). Say that `c.is_alpha()` is Unicode or ASCII, and add `is_ascii_*` if those exist. Write "`n.to_str()`" explicitly next to the `to_string` habit.
- **`ail ask how`:** add an entry for "parse a fixed-point decimal / money amount without floats". Character-by-character validation with digit limits is common in these test apps, and turning a digit `char` into an int currently takes `"{c}".to_int()?` or `c.to_str().to_int()?`. A `c.to_digit()` returning `int?` would help, or documenting one if it exists.
- **Training examples:** line-oriented command interpreters that show:
  - `words()` tokenizing
  - an `if`/`elif` expression used as a value (I relied on `expected := if ... 2 elif ...` working; that guess paid off, but I saw no example of it)
  - `elif amt := parse(x)` binding inside an `elif` chain
  - a `Map[str, Struct]` updated in place
  - multi-key sorts with a descending numeric key
  - fixed-width table output

5. AIL for agentic coding

Easier or safer, because of the language:
- `T?` with `if x := ...`/`else` forced a deliberate path for invalid amounts.
- Overflow traps instead of wrapping silently.
- Stable sort with tuple keys removed comparator bugs.
- Maps keep insertion order, so behaviour is deterministic.
- Strict 4-space blocks and `if`-as-expression kept the dispatch compact.
- The compiler fixing known foreign habits in place, and naming the rule, saves whole edit–check rounds, which matters with a limited turn budget.

Harder, because of the language: strings have no indexing, so the parsing goes through `chars()` lists, and turning a char into a digit is clumsy. These are minor.

Harder, because I didn't know it: I had to look up method names (`words`, `pad_right`, `to_str`) and check edge semantics (whitespace definition, padding overflow) that I would simply know in Python or Rust. Most of my lookup turns went to that. The one place I didn't look it up (padding overflow) is the one place my program has untested risk.

Overall the whole job took about 10 tool calls with one compile fix. That compares well with doing it in a familiar language, and it is mostly thanks to the compact card.

## Builder's self-report: Python

**1. Result and evidence**

The ledger is in `work/app.py`, written in Python 3 with only the standard library. I ran it twice:

- **Public case `errors_and_close`:** the output matched the expected output byte for byte, including both reports, the five error lines and `ok=7 errors=6`.
- **My own edge-case input:** this covered:
  - leading tabs and spaces, and a comment line that starts with a tab;
  - a 12-character name (accepted), a 13-character name and a name starting with a digit (both rejected);
  - a kind in the wrong case (`Asset`);
  - an amount of exactly 10^12 cents (accepted) and one cent over (rejected);
  - `-0.00`, a leading zero (`012.00`), `-` on its own and `5.`;
  - a move to the same account, an unknown account and a negative move amount;
  - closing an account that doesn't exist, then opening and closing an account before a report.

  I checked every line of that output against the spec by hand and found no mismatch. It also showed that a balance wider than its column prints in full and that the sort works on ties.

I did not run the other two public cases (`worked_example` and `sort_ties`), and I did not try empty input. Their logic is covered by the runs above, but they were not run exactly as given. I would run them before relying on this.

**2. What took more than one try**

Nothing. The first version passed every test I ran, so I made no changes. Places where I deliberately followed the spec closely:
- I split tokens on spaces and tabs only, not on all whitespace.
- I used `fullmatch` so a trailing newline can't slip past a `$` in the patterns.
- `MOVE` checks both accounts exist before checking whether they are the same one.
- The 10^12 limit is checked separately from the 11-digit pattern, because 11 digits can be up to about 10^13 cents.

**3. Bugs found by running, and bugs a stricter compiler could have caught**

- **Found by running:** none. Both runs gave correct output the first time.
- **For a stricter compiler:** none came up, because there were no bugs. Python has no compile step before running, so the only checks were the test runs. A type checker such as mypy would mostly check that the account records (`[kind, balance, posts]` lists) and the amount parser's `None` return are handled correctly. The code already checks for `None` before using an amount.

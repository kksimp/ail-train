# Browser queue 1 (local model, Garlic CSS/HTML gaps)

Where: `tools/garlic/` in the AIL repo (kksimp/ail). CSS properties are listed in `USED` in
`tools/garlic/css/css.ail` (line ~57) and applied in `tools/garlic/page/page.ail` (~line 485-560).
Tests: `./ail test tools/garlic/garlic.ail`. Text view: `./ail run tools/garlic/garlic.ail --print FILE`.
Test pages live in `tools/garlic/testdata/`.

## Rules for the loop (the supervising agent plans, the local model types)
1. For each task, the supervisor FIRST writes a failing test (or an `--print` expected-output
   check) and shows it fails. The local model never writes the test.
2. Give the model only the 1-2 files involved, and name the exact anchor line to edit.
3. Gate: new test passes, `./ail check` passes, `./ail test tools/garlic/garlic.ail` has no new failures.
4. At most 2 retries, feeding back the failure output. Then stop and record what went wrong.
5. One commit per task on a local scratch branch. No push or PR without Kaleb's go-ahead.
6. Cite the spec rule id in code and diagnostics (AGENTS.md). No model names in committed files.
7. Do not touch graphics/layout architecture. That is the supervising agent's design work.

## Tasks (small, independent; supervisor confirms current behaviour before starting)
1. `text-transform: lowercase` and `capitalize` (today only `uppercase` is handled, `style.upper`).
2. `hidden` HTML attribute: element is dropped like `display: none`.
3. `display: none` on the `<head>`-like and `<template>` elements; `<template>` content never shown.
4. `list-style: none` / `list-style-type: none` suppresses the bullet or number in lists.
5. `font-weight: normal` / `lighter` overrides `<b>`, `<strong>` and `<th>` defaults (check the current code).
6. `white-space: nowrap` keeps a run on one line (no wrapping) in text cells.
7. `visibility: collapse` treated like `hidden`.
8. `display: inline-block` / `inline` handled like `inline` for a `<div>` (supervisor decides expected text output).

Add new CSS properties to `USED` only together with the code that applies them. After 8 tasks,
the supervisor reports pass rate, retries, wall time and what the model got wrong.

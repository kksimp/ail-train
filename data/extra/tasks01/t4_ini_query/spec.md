# INI query

Standard input has two parts separated by a line that is exactly `---` (after trimming spaces): an INI document, then
a list of queries, one per line.

INI lines (trim spaces first):
- empty lines and lines starting with `;` or `#` are ignored;
- `[name]` starts section `name` (the text inside the brackets, trimmed); keys before any section belong to the section
  with the empty name;
- `key = value` sets `key` (text before the first `=`, trimmed) to `value` (the rest, trimmed, possibly empty) in the
  current section; a later assignment of the same section and key replaces the earlier one;
- any other line (no `=`, or an empty key) is ignored.
Section names and keys never contain `.`.

A query is `section.key` (the empty section is written `.key`). For each non-blank query line (trimmed) print the
value, or `(missing)` if that section/key was never set, or `(bad query)` if the query has no `.`.
Blank query lines are skipped. If there is no `---` line there are no queries and nothing is printed.

Example input:
    name = demo
    [db]
    host = localhost
    port=5432
    ---
    db.port
    .name
    db.user

Example output:
    5432
    demo
    (missing)

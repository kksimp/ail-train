Read invoice lines from standard input, one per line: `description,qty,unit_cents,code`. Blank lines are ignored.
`qty` is an integer >= 1, `unit_cents` an integer >= 0 (both trimmed), `code` (trimmed) is one of the tax codes
A, B, C, D with rates A = 0%, B = 5%, C = 8.25%, D = 10%. The description (trimmed) must be non-empty and there must be
exactly 4 fields. Any other line prints `line N: invalid` (N is the 1-based line number, blank lines counted) and is skipped.

For each valid line: net = qty * unit_cents; tax = net * rate rounded half up to whole cents, computed as
(net * rate_in_basis_points + 5000) / 10000 with integer division (basis points: 0, 500, 825, 1000).
Print `DESC: net=N tax=T (CODE)` per valid line in input order. Then print `subtotal: S`, then one line
`tax CODE: X` for each code that appears in at least one valid line, in alphabetical order of code (X is the sum of the
per-line taxes), then `total: G` (subtotal plus all tax). Money is dollars with two decimals (`1205` -> `12.05`).

Example input:
    widget,3,1999,B
    manual,1,500,A
Output:
    widget: net=59.97 tax=3.00 (B)
    manual: net=5.00 tax=0.00 (A)
    subtotal: 64.97
    tax A: 0.00
    tax B: 3.00
    total: 67.97

With no valid lines the output is `subtotal: 0.00` and `total: 0.00`.

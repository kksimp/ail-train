import sys

rows = [l.split(",") for l in sys.stdin.read().split("\n") if l != ""]
if rows:
    ncol = max(len(r) for r in rows)
    rows = [r + [""] * (ncol - len(r)) for r in rows]
    widths = [max(len(r[c]) for r in rows) for c in range(ncol)]
    def fmt(r):
        return " | ".join(r[c].ljust(widths[c]) for c in range(ncol)).rstrip()
    print(fmt(rows[0]))
    print("-+-".join("-" * w for w in widths))
    for r in rows[1:]:
        print(fmt(r))

def collapse(cs):
    kept = []
    for c in cs:
        top = kept[-1] if kept else ' '
        if top != c and top.upper() == c.upper():
            kept.pop()
        else:
            kept.append(c)
    return len(kept)

chain = list("gKkMmTxXtBpPbHqQRrhaAgGjJyYcdDCgNqRsLmSsl")
print(f"{len(chain)} units, {collapse(chain)} after reacting")
print(f"part 1: {collapse(chain)}")
best = len(chain); drop = ' '
for code in range(65, 91):
    up = chr(code)
    n = collapse([c for c in chain if c.upper() != up])
    if n < best:
        best = n; drop = up
print(f"part 2: removing {drop} leaves {best}")

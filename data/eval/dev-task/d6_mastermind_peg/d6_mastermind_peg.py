import sys

lines = sys.stdin.read().splitlines()
if lines:
    secret = lines[0].strip()
    for raw in lines[1:]:
        g = raw.strip()
        if g == "":
            continue
        if len(g) != 4 or any(c not in "ABCDEF" for c in g):
            print(g + " invalid")
            continue
        black = sum(1 for a, b in zip(secret, g) if a == b)
        total = sum(min(secret.count(c), g.count(c)) for c in "ABCDEF")
        white = total - black
        out = f"{g} {black} {white}"
        if black == 4:
            out += " solved"
        print(out)

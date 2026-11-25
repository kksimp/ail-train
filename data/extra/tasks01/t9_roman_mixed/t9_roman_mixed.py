import sys

PAIRS = [(1000, "M"), (900, "CM"), (500, "D"), (400, "CD"), (100, "C"), (90, "XC"),
         (50, "L"), (40, "XL"), (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")]
VAL = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}


def to_roman(n):
    out = ""
    for v, s in PAIRS:
        while n >= v:
            out += s
            n -= v
    return out


def parse(tok):
    if tok != "" and all(c in "0123456789" for c in tok):
        if tok[0] == "0" or len(tok) > 4:
            return None
        n = int(tok)
        return n if 1 <= n <= 3999 else None
    if tok != "" and all(c in VAL for c in tok):
        total = 0
        for i, c in enumerate(tok):
            if i + 1 < len(tok) and VAL[c] < VAL[tok[i + 1]]:
                total -= VAL[c]
            else:
                total += VAL[c]
        if 1 <= total <= 3999 and to_roman(total) == tok:
            return total
    return None


good = []
bad = []
for k, line in enumerate(sys.stdin.read().split("\n"), 1):
    if line.strip(" ") == "":
        continue
    if "." not in line:
        bad.append((k, line))
        continue
    tok, text = line.split(".", 1)
    n = parse(tok)
    if n is None:
        bad.append((k, line))
        continue
    good.append((n, text.strip(" ")))
good.sort(key=lambda g: g[0])
for n, text in good:
    print(("%d %s %s" % (n, to_roman(n), text)).rstrip(" "))
for k, line in bad:
    print("invalid line %d: %s" % (k, line))

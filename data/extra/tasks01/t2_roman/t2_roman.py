import sys

TABLE = [(1000, "M"), (900, "CM"), (500, "D"), (400, "CD"), (100, "C"), (90, "XC"),
         (50, "L"), (40, "XL"), (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")]
VAL = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

def to_roman(n):
    out = ""
    for v, s in TABLE:
        while n >= v:
            out += s
            n -= v
    return out

def from_roman(t):
    total = 0
    for i, c in enumerate(t):
        v = VAL[c]
        if i + 1 < len(t) and VAL[t[i + 1]] > v:
            total -= v
        else:
            total += v
    return total

def main():
    lines = sys.stdin.read().split("\n")
    if lines[-1] == "":
        lines.pop()
    done = 0
    for k, raw in enumerate(lines, 1):
        t = raw.strip()
        if t == "":
            continue
        if t.isascii() and t.isdigit():
            if len(t.lstrip("0")) > 6 or not (1 <= int(t) <= 3999):
                print(f"line {k}: out of range")
            else:
                print(to_roman(int(t)))
                done += 1
        elif all(c in VAL for c in t):
            v = from_roman(t)
            if v >= 1 and to_roman(v) == t:
                print(v)
                done += 1
            else:
                print(f"line {k}: not canonical {t}")
        else:
            print(f"line {k}: invalid")
    print(f"converted {done}")

main()

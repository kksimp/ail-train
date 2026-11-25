import re, sys

def mean_text(s, k):
    h = abs(s) * 100 // k
    sign = "-" if s < 0 and h > 0 else ""
    return f"{sign}{h // 100}.{h % 100:02d}"

def main():
    lines = sys.stdin.read().split("\n")
    if lines and lines[-1] == "":
        lines.pop()
    k = 0
    s = 0
    lo = hi = 0
    for i, raw in enumerate(lines, 1):
        t = raw.strip(" \t\r")
        if t == "":
            continue
        if not re.fullmatch(r"-?[0-9]{1,9}", t):
            print(f"bad line {i}")
            continue
        n = int(t)
        if k == 0:
            lo = hi = n
        else:
            lo = min(lo, n)
            hi = max(hi, n)
        k += 1
        s += n
        print(f"{k}: sum={s} min={lo} max={hi} mean={mean_text(s, k)}")
    print("no data" if k == 0 else f"done {k}")

main()

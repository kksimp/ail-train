import sys


def num(s):
    if s.isascii() and s.lstrip("-").isdigit() and s != "-":
        return int(s)
    return None


def main():
    lines = sys.stdin.read().split("\n")
    if lines[-1] == "":
        lines.pop()
    w = lines[0].split() if lines else []
    n = num(w[1]) if len(w) == 2 and w[0] == "servers" else None
    if n is None or not 1 <= n <= 9:
        print("bad header")
        return
    free = [0] * n
    last = 0
    served = tw = mw = fin = 0
    for k, line in enumerate(lines[1:], 2):
        w = line.split()
        if not w:
            continue
        t = num(w[1]) if len(w) == 4 and w[0] == "arrive" else None
        s = num(w[3]) if len(w) == 4 else None
        if t is None or s is None or t < 0 or s < 1:
            print(f"line {k}: bad line")
            continue
        if t < last:
            print(f"line {k}: out of order")
            continue
        last = t
        start = max(t, min(free))
        cands = [i for i in range(n) if free[i] <= start]
        i = cands[0] if cands else free.index(min(free))
        free[i] = start + s
        wait = start - t
        served += 1
        tw += wait
        mw = max(mw, wait)
        fin = max(fin, start + s)
        print(f"{w[2]} server {i + 1} start {start} end {start + s} wait {wait}")
    print(f"served {served} total_wait {tw} max_wait {mw} finish {fin}")


main()

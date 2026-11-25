import re, sys

def main():
    vals = []
    skipped = 0
    for t in sys.stdin.read().split():
        if re.fullmatch(r"-?[0-9]{1,9}", t):
            vals.append(int(t))
        else:
            skipped += 1
    if not vals:
        print("no values")
        print(f"skipped {skipped}")
        return
    n = len(vals)
    s = sum(vals)
    h = abs(s) * 100 // n
    mean = ("-" if s < 0 and h > 0 else "") + f"{h // 100}.{h % 100:02d}"
    v = sorted(vals)
    if n % 2 == 1:
        med = str(v[n // 2])
    else:
        t = v[n // 2 - 1] + v[n // 2]
        if t % 2 == 0:
            med = str(t // 2)
        else:
            a = abs(t) // 2
            med = ("-" if t < 0 else "") + f"{a}.5"
    counts = {}
    for x in vals:
        counts[x] = counts.get(x, 0) + 1
    best = min(counts, key=lambda k: (-counts[k], k))
    print(f"count {n}")
    print(f"sum {s}")
    print(f"min {v[0]}")
    print(f"max {v[-1]}")
    print(f"mean {mean}")
    print(f"median {med}")
    print(f"mode {best} (x{counts[best]})")
    print(f"skipped {skipped}")

main()

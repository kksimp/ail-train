import sys


def digits(s):
    return s.isascii() and s.isdigit()


def main():
    lines = [l for l in sys.stdin.read().splitlines() if l != ""]
    h = lines[0].split(" ") if lines else []
    if len(h) != 2 or h[0] != "window" or not digits(h[1]) or int(h[1]) < 1:
        print("error: bad header")
        return
    w = int(h[1])
    ref = {}
    drops = {}
    kept = bad = dropped = 0
    last = 0
    for line in lines[1:]:
        f = line.split(" ", 2)
        if len(f) < 2 or not digits(f[0]) or f[1] == "" or int(f[0]) < last:
            bad += 1
            continue
        t = int(f[0])
        last = t
        k = f[1]
        if k in ref and t - ref[k] < w:
            dropped += 1
            drops[k] = drops.get(k, 0) + 1
        else:
            ref[k] = t
            kept += 1
            print(line)
    print(f"kept: {kept} dropped: {dropped} malformed: {bad}")
    for k in sorted(drops):
        print(f"{k} {drops[k]}")


main()

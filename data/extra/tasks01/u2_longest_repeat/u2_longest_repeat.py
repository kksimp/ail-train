import sys

def main():
    words = [w.lower() for w in sys.stdin.read().split()]
    n = len(words)
    for L in range(n - 1, 0, -1):
        seen = {}
        for i in range(0, n - L + 1):
            g = " ".join(words[i:i + L])
            seen.setdefault(g, []).append(i + 1)
        for g, pos in seen.items():
            if len(pos) >= 2:
                print(f"length={L}")
                print(f"text={g}")
                print("starts=" + ",".join(str(p) for p in pos))
                return
    print("none")

main()

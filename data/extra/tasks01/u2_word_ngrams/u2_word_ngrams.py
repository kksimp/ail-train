import sys

def main():
    text = sys.stdin.read()
    lines = text.splitlines()
    if not lines:
        print("no input")
        return
    t = lines[0].strip()
    if t not in ("1", "2", "3"):
        print("bad n")
        return
    n = int(t)
    words = []
    for ln in lines[1:]:
        for w in ln.split():
            words.append(w.lower())
    counts = {}
    total = 0
    for i in range(0, len(words) - n + 1):
        g = " ".join(words[i:i + n])
        counts[g] = counts.get(g, 0) + 1
        total += 1
    for g in sorted(counts, key=lambda k: (-counts[k], k))[:5]:
        print(f"{counts[g]} {g}")
    print(f"distinct={len(counts)} total={total}")

main()

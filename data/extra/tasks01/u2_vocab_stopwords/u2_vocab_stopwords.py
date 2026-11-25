import sys

def main():
    lines = sys.stdin.read().splitlines()
    if not lines:
        print("no input")
        return
    stops = set()
    for s in lines[0].split(","):
        s = s.strip().lower()
        if s:
            stops.add(s)
    words = []
    cur = []
    for ch in "\n".join(lines[1:]).lower() + "\n":
        if "a" <= ch <= "z":
            cur.append(ch)
        else:
            if cur:
                words.append("".join(cur))
            cur = []
    counts = {}
    stopped = 0
    total = 0
    for w in words:
        if w in stops:
            stopped += 1
        else:
            counts[w] = counts.get(w, 0) + 1
            total += 1
    for w in sorted(counts, key=lambda k: (-counts[k], k)):
        print(f"{w} {counts[w]}")
    print(f"total={total} unique={len(counts)} stopped={stopped}")

main()

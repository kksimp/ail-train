import sys

def main():
    lines = sys.stdin.read().splitlines()
    count = {}
    first = {}
    total = 0
    for i, ln in enumerate(lines, 1):
        runs = []
        cur = []
        for ch in ln + " ":
            if ("a" <= ch <= "z") or ("A" <= ch <= "Z"):
                cur.append(ch)
            else:
                if cur:
                    runs.append("".join(cur))
                cur = []
        for r in runs:
            if 2 <= len(r) <= 6 and r == r.upper():
                if r not in count:
                    count[r] = 0
                    first[r] = i
                count[r] += 1
                total += 1
    if not count:
        print("no acronyms")
        return
    for r in count:
        print(f"{r} {count[r]} {first[r]}")
    print(f"total={total} distinct={len(count)}")

main()

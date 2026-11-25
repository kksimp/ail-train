import sys

students = []
for i, line in enumerate(sys.stdin.read().split("\n"), 1):
    line = line.rstrip("\r")
    if line.strip() == "":
        continue
    f = line.split(",")
    name = f[0].strip()
    ok = name != "" and len(f) >= 2
    scores = []
    if ok:
        for s in f[1:]:
            s = s.strip()
            if not (s.isascii() and s.isdigit()) or int(s) > 100:
                ok = False
                break
            scores.append(int(s))
    if not ok:
        print(f"line {i}: invalid")
        continue
    if len(scores) >= 4:
        scores.remove(min(scores))
    n = len(scores)
    avg = (sum(scores) * 20 + n) // (2 * n)
    students.append((name, avg))

students.sort(key=lambda s: (-s[1], s[0].encode()))
counts = {"A": 0, "B": 0, "C": 0, "D": 0, "F": 0}
for name, avg in students:
    g = "A" if avg >= 900 else "B" if avg >= 800 else "C" if avg >= 700 else "D" if avg >= 600 else "F"
    counts[g] += 1
    print(f"{name}: avg={avg // 10}.{avg % 10} grade={g}")
print("grades: " + " ".join(f"{k}={counts[k]}" for k in "ABCDF"))

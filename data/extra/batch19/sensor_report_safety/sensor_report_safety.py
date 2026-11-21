def safe(xs):
    if len(xs) < 2: return True
    rising = xs[1] > xs[0]
    for i in range(1, len(xs)):
        d = xs[i] - xs[i - 1] if rising else xs[i - 1] - xs[i]
        if d < 1 or d > 3: return False
    return True

def dampened(xs):
    if safe(xs): return True
    return any(safe(xs[:i] + xs[i + 1:]) for i in range(len(xs)))

reports = ["3 5 6 9 11", "20 18 17 13 12", "4 6 5 7 8", "9 7 6 4 1", "1 1 2 3 4", "15 12 10 9 9 6", "2 5 8 7 10", "30 31 29 28 25"]
p1 = p2 = 0
for r in reports:
    xs = [int(w) for w in r.split(" ")]
    a = safe(xs); b = dampened(xs)
    verdict = "safe" if a else ("safe with one dropped" if b else "unsafe")
    print(f"{r:<16} {verdict}")
    if a: p1 += 1
    if b: p2 += 1
print(f"part 1: {p1} safe reports")
print(f"part 2: {p2} safe with the dampener")

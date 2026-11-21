def rating(n):
    return "simple" if n <= 4 else "moderate" if n <= 7 else "complex"

src = ["fn clamp(x, lo, hi)", "    if x < lo", "        return lo", "    if x > hi", "        return hi", "    return x", "fn grade(score)", "    if score >= 90 and bonus", "        return A", "    elif score >= 80 or extra", "        return B", "    elif score >= 70", "        return C", "    return F", "fn scan(rows)", "    for r in rows", "        while r.busy", "            if r.ok and r.ready or r.forced", "                send(r)", "            elif r.late", "                drop(r)", "    return done", "fn hello()", "    print(hi)"]
decision = ["if", "elif", "while", "for", "and", "or"]
names = []
scores = []
for line in src:
    if line.startswith("fn "):
        names.append(line[3:].split("(")[0])
        scores.append(1)
    else:
        hits = len([w for w in line.split() if w in decision])
        scores[-1] += hits
for i, n in enumerate(names):
    print(f"{n:<6} {scores[i]:>2}  {rating(scores[i])}")
worst = names[scores.index(max(scores))]
print(f"refactor first: {worst}")

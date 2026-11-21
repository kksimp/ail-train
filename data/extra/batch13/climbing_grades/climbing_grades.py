yds = ["5.9", "5.10a", "5.10b", "5.10c", "5.10d", "5.11a", "5.11b", "5.11c", "5.11d", "5.12a"]
french = ["5c", "6a", "6a+", "6b", "6b+", "6c", "6c+", "7a", "7a+", "7b"]
sends = ["5.10a", "5.9", "5.10c", "5.10a", "5.11a", "5.10b", "5.9", "5.10c", "5.10a", "5.11c", "5.10b", "5.9", "5.10c", "5.13a"]
counts = {}
unknown = []
for s in sends:
    if s in yds:
        i = yds.index(s)
        counts[i] = counts.get(i, 0) + 1
    else:
        unknown.append(s)
grades = sorted(counts.keys())[::-1]
for g in grades:
    bar = "#" * counts[g]
    print(f"{yds[g]:<6} {french[g]:<4} {bar}")
top = grades[0]
print(f"hardest send: {yds[top]} ({french[top]}), {len(sends) - len(unknown)} sends graded")
if unknown:
    missing = ", ".join(unknown)
    print(f"not in the table: {missing}")

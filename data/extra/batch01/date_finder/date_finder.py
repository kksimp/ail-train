import re
r = re.compile(r"(\d{4})-(\d{2})-(\d{2})")
notes = ["Kick-off 2024-03-05, review 2024-04-19.", "Holiday from 2023-12-22 to 2024-01-02", "no dates here", "Deadline 2025-06-30"]
py = {}
for n in notes:
    f = [m.group(0) for m in r.finditer(n)]
    print(f"{len(f)}: {' '.join(f)}")
    print("   " + r.sub(r"\3/\2/\1", n))
    for d in f:
        py[d[:4]] = py.get(d[:4], 0) + 1
for y in sorted(py):
    print(f"{y}: {py[y]}")

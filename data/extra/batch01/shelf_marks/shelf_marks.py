def parse_mark(text):
    words = text.split()
    if len(words) != 3:
        return None
    nums = words[1].split(".")
    try:
        whole = int(nums[0])
        part = int(nums[1]) if len(nums) > 1 else 0
    except ValueError:
        return None
    return (words[0], whole, part, words[2])

raw = ["QA 76.9 B12", "PS 3545 W5", "QA 76.73 P98", "QA 9 A1", "PS 3545.2 A3", "Z 1 x.y Q", "QA 76.9 A7"]
marks = []
for r in raw:
    m = parse_mark(r)
    if m:
        marks.append(m)
    else:
        print(f"skipped: {r}")
for m in sorted(marks):
    print(f"{m[0]} {m[1]}.{m[2]} {m[3]}")
counts = {}
for m in marks:
    counts[m[0]] = counts.get(m[0], 0) + 1
for k, n in counts.items():
    print(f"{k}: {n}")

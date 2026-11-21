times = [5, 20, 50, 55, 57, 58, 59, 61, 62, 63, 64, 65, 66, 100, 130]
limit = 5
counts = {}
allowed = []
for t in times:
    w = t // 60
    if counts.get(w, 0) < limit:
        counts[w] = counts.get(w, 0) + 1
        allowed.append(t)
        print(f"t={t:>3} window {w} call {counts[w]} allowed")
    else:
        print(f"t={t:>3} window {w} rejected")
worst = 0
worst_at = 0
for s in allowed:
    inside = sum(1 for x in allowed if x >= s and x < s + 60)
    if inside > worst:
        worst = inside
        worst_at = s
print(f"busiest 60 s span starts at {worst_at} with {worst} calls (limit {limit})")

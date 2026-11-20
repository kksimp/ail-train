today = 100
p = [("milk", 102), ("yoghurt", 98), ("rice", 400), ("eggs", 106), ("bread", 100), ("cheese", 95), ("jam", 160)]
def bucket(d): return "expired" if d < 0 else "this week" if d <= 6 else "later"
g = {}
for n, b in sorted(p, key=lambda x: (x[1], x[0])):
    g.setdefault(bucket(b - today), []).append(f"{n} ({b - today})")
for b in ["expired", "this week", "later"]:
    print(f"{b}: {', '.join(g.get(b, []))}")
print(f"throw out: {sum(1 for _, b in p if b < today)}")

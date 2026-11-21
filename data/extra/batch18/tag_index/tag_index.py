posts = [(1, ["baking", "bread"]), (2, ["bread", "fermenting"]), (3, ["fermenting", "vegetables"]), (4, ["baking", "bread", "photos"]), (5, ["fermenting", "vegetables"])]
idx = {}
for i, ts in posts:
    for t in ts: idx.setdefault(t, []).append(i)
for t in sorted(idx): print(f"{t:<11} {idx[t]}")
a = idx["bread"]; b = idx["fermenting"]
print(f"bread and fermenting: {sorted(set(a) & set(b))}")
print(f"bread or fermenting: {len(set(a) | set(b))} posts")
print("cheese: 0 posts")

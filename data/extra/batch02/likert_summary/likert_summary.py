L = ["SD", "D", "N", "A", "SA"]
ans = {"The app is easy to use": [5, 4, 4, 3, 5, 2, 4, 5], "Support was helpful": [2, 3, 1, 2, 4, 3, 2, 2], "I would recommend it": [4, 4, 5, 5, 3, 4, 4, 1]}
for q, xs in ans.items():
    d = " ".join(f"{L[k - 1]}:{xs.count(k)}" for k in range(1, 6))
    print(q)
    print(f"  {d} | mean {sum(xs) / len(xs):.2f} | agree {sum(1 for x in xs if x >= 4) * 100 // len(xs)}%")
print(f"highest rated: {max(ans, key=lambda q: sum(ans[q]))}")

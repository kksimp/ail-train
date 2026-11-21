q = [(1840, "Brightway", 5), (1525, "Allied", 12), (2210, "Crest", 3), (1525, "Delta", 7), (1690, "Evergreen", 9), (2050, "Fenwick", 4)]
s = sorted(q)
for i in range(3): print(f"{i + 1}. {s[i][1]:<10} {s[i][0]} ({s[i][2]} days)")
print(f"{len(q) - 3} quotes left in the heap")
d = max(q)
print(f"dearest: {d[1]} at {d[0]}")
print(f"prices with 5 days or less: {sorted(x[0] for x in q if x[2] <= 5)}")

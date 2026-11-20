orders = [(1001, 7, 2599), (1002, 9, 1250), (1003, 7, 899), (1004, 12, 4000)]
spent = {}
for i, c, ct in orders:
    spent[c] = spent.get(c, 0) + ct
for c, ct in spent.items():
    print(f"customer {c}: {ct} cents over " + ", ".join(f"#{i}" for i, cc, _ in orders if cc == c))
print(f"top customer: {max(spent, key=lambda k: spent[k])}")
print("true")

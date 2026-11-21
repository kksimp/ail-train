th = [(1, 0, "ola", "Has anyone tried the new trail?"), (2, 1, "ben", "Yes, muddy after rain"), (3, 2, "ola", "Boots it is then"), (4, 1, "kit", "The view at the top is worth it"), (5, 3, "ben", "And gaiters"), (6, 0, "dee", "Car park full by 9 on Sundays")]
par = {c[0]: c[1] for c in th}
def depth(i):
    u = par.get(i, 0)
    return 0 if u == 0 else 1 + depth(u)
for c in th: print(f"{'  ' * depth(c[0])}{c[2]}: {c[3]}")
print(f"deepest reply is {max(depth(c[0]) for c in th)} levels down")
print(f"{sum(1 for c in th if c[1] == 0)} top-level comments")

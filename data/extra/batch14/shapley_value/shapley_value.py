from itertools import permutations
from math import gcd
def worth(kind, members):
    if kind == 0:
        needs = [10, 20, 30, 60]
        return max([0] + [needs[m] for m in members])
    lefts = len([m for m in members if m == 0])
    rights = len([m for m in members if m > 0])
    return min(lefts, rights) * 12
def shapley(kind, n, names):
    orders = list(permutations(range(n)))
    share = [0] * n
    for order in orders:
        present = []
        for p in order:
            before = worth(kind, present)
            present.append(p)
            share[p] += worth(kind, present) - before
    for i in range(n):
        g = gcd(share[i], len(orders))
        exact = share[i] / len(orders)
        den = len(orders) // g
        et = f"{share[i] // g}" if den == 1 else f"{share[i] // g}/{den}"
        print(f"    {names[i]:<8} {et} = {exact:.2f}")
print("airstrip costing the longest need (10, 20, 30, 60):")
shapley(0, 4, ["glider", "prop", "turbo", "jet"])
print("one left glove and two right gloves, a pair sells for 12:")
shapley(1, 3, ["left", "right A", "right B"])

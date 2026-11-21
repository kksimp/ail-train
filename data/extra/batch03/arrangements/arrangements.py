from itertools import permutations
a = sorted("".join(p) for p in permutations("abc"))
print(f"abc: {len(a)} orders: {' '.join(a)}")
for w in ["abcd", "aab", "noon", "level"]:
    o = ["".join(p) for p in permutations(w)]
    print(f"{w}: {len(o)} orders, {len(set(o))} distinct")

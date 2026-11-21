nr = lambda s: (s * 48271) % 2147483647
def sh(xs, seed):
    out = list(xs); s = seed; i = len(out) - 1
    while i > 0:
        s = nr(s); j = s % (i + 1); out[i], out[j] = out[j], out[i]; i -= 1
    return out
people = ["Ana", "Ben", "Cat", "Dan", "Eva", "Fin"]
pt = {"Ana": "Ben", "Ben": "Ana", "Cat": "Dan", "Dan": "Cat"}
seed = 7; tries = 0
while True:
    tries += 1; seed = nr(seed); tk = sh(people, seed)
    if all(g != t and pt.get(g, "") != t for g, t in zip(people, tk)): break
print(f"valid draw after {tries} tries:")
for g, t in zip(people, tk):
    print(f"  {g} -> {t}")

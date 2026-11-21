P = "the fog comes\non little cat feet\nit sits looking\nover harbor and city\non silent haunches\nand then moves on"; seen = set(); b = ""; bs = 0.0
for l in P.split("\n"):
    L = [c for c in l if c.isalpha()]; v = sum(1 for c in L if c in "aeiou"); s = v / len(L)
    print(f"{l:<22} vowels {v:>2}, consonants {len(L) - v:>2}")
    if s > bs: bs = s; b = l
    seen |= set(L)
print(f"most vowel-heavy: {b} ({bs:.2f})")
print("unused: " + "".join(chr(c) for c in range(97, 123) if chr(c) not in seen))

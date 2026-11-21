for a, b in [("GAGCCTACTAACGGGAT", "CATCGTAATGACGGCCT"), ("10110110", "10011010"), ("AAAA", "AAAA")]:
    d = [i for i in range(len(a)) if a[i] != b[i]]; print(f"{a} vs {b}: {len(d)} at [{','.join(map(str, d))}]")
t = sum(bin(x ^ y).count("1") for x in range(16) for y in range(16)); print(f"mean distance of 4-bit pairs: {t / 256:.2f}")

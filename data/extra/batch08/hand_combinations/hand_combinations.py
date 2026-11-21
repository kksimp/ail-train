from math import comb
t = comb(52, 5); print(f"all hands: {t}")
for n, c in [("four of a kind", 13 * comb(4, 4) * 48), ("full house", 13 * comb(4, 3) * 12 * comb(4, 2)), ("flush (incl. straight flushes)", 4 * comb(13, 5)), ("three of a kind", 13 * comb(4, 3) * comb(12, 2) * 16), ("two pair", comb(13, 2) * comb(4, 2) * comb(4, 2) * 44), ("one pair", 13 * comb(4, 2) * comb(12, 3) * 64)]:
    print(f"{n}: {c} hands, 1 in {(t + c // 2) // c}")

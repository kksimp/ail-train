P = A = 0
for n, p, s in [("rent", 950, 950), ("food", 320, 371), ("transport", 120, 98), ("energy", 140, 162), ("fun", 100, 87), ("phone", 30, 30), ("gifts", 40, 75)]:
    P += p; A += s; d = s - p; pc = int(d * 1000 / p); sg = "+" if d > 0 else ""
    print(f"{n:<10} {p:>4} {s:>4} {sg}{d} ({sg}{int(pc / 10)}.{abs(pc) % 10}%){' OVER' if pc > 100 else ''}")
print(f"total plan {P}, spent {A}, difference {A - P}")

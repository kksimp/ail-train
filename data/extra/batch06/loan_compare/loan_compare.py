def pm(a, r, y):
    r = r / 12.0; n = float(y * 12)
    return a / n if r == 0.0 else a * r / (1.0 - (1.0 + r) ** -n)
b = ""; bc = 1e6
for n, a, r, y in [("bank", 15000.0, 0.069, 5), ("credit union", 15000.0, 0.055, 6), ("dealer", 15000.0, 0.0, 4), ("online", 15000.0, 0.049, 7)]:
    p = pm(a, r, y); i = p * float(y * 12) - a; print(f"{n:<12} {p:>8.2f}/month over {y} years, interest {i:>8.2f}")
    if i < bc: bc = i; b = n
print(f"cheapest: {b}")

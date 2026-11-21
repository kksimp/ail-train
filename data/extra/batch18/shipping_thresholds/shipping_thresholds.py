def charge(t, kg, z):
    if kg > 30: return None
    if z == 0 and t >= 5000: return 0
    return (395 + 120 * kg) * [1, 2, 4][z]
def money(c): return f"{c // 100}.{c % 100:02}"
Z = ["UK", "EU", "World"]; fees = 0
for t, kg, z in [(3200, 2, 0), (5400, 6, 0), (5400, 6, 1), (1250, 1, 2), (8900, 31, 0), (4999, 12, 0)]:
    c = charge(t, kg, z)
    if c is not None:
        fees += c; s = "free" if c == 0 else money(c)
        print(f"{money(t):>6} {kg:>2} kg {Z[z]:<5} delivery {s}")
    else: print(f"{money(t):>6} {kg:>2} kg {Z[z]:<5} too heavy, over 30 kg")
print(f"delivery income {money(fees)}")

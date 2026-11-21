def otb_of(p, opening): return p[1] + p[3] + p[2] - opening - p[4]
opening = 120000
plans = [("Aug", 64000, 3000, 135000, 52000), ("Sep", 71000, 2500, 150000, 30000), ("Oct", 82000, 4000, 165000, 95000), ("Nov", 98000, 6000, 140000, 20000), ("Dec", 120000, 15000, 90000, 0)]
total = 0
for p in plans:
    otb = otb_of(p, opening)
    state = f"over-bought by {-otb}" if otb < 0 else f"may yet buy {otb}"
    print(f"{p[0]}: open {opening:>6}, sales {p[1]:>6}, close {p[3]:>6}, on order {p[4]:>5}: {state}")
    total += otb
    opening = p[3]
print(f"season open to buy {total}")

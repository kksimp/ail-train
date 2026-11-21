def half_kilos(g): return (g + 499) // 500
def chargeable(p):
    vol = p[1] * p[2] * p[3] // 5
    return half_kilos(max(vol, p[4]))
rate_first = 650; rate_extra = 180
parcels = [("P1", 30, 20, 15, 2100), ("P2", 60, 40, 40, 3500), ("P3", 25, 25, 10, 4800), ("P4", 100, 30, 30, 6200), ("P5", 40, 30, 20, 4800)]
total = 0
for p in parcels:
    vol = p[1] * p[2] * p[3] // 5
    units = chargeable(p)
    cost = rate_first + (units - 1) * rate_extra
    total += cost
    basis = "volume" if vol > p[4] else "weight"
    print(f"{p[0]}: actual {p[4]} g, volumetric {vol} g -> {units // 2}.{units % 2 * 5} kg by {basis}, {cost // 100}.{cost % 100:02}")
print(f"total {total // 100}.{total % 100:02}")

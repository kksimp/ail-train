def settle(parts):
    heat = 0.0; cap = 0.0
    for p in parts:
        heat += p[1] * p[2] * p[3]
        cap += p[1] * p[2]
    return heat / cap
hot = 60.0; cold = 12.0; target = 40.0
share = (target - cold) / (hot - cold)
litres = 150.0
print(f"hot share for {target:.0f} C: {share * 100.0:.1f}% ({share * litres:.1f} L of {litres:.0f} L)")
water = [("hot", share * litres, 4.186, hot), ("cold", (1.0 - share) * litres, 4.186, cold)]
print(f"water alone settles at {settle(water):.2f} C")
tub = water + [("steel tub", 60.0, 0.49, 15.0)]
t = settle(tub)
print(f"in a 60 kg steel tub at 15 C: {t:.2f} C")
extra = (target - t) * (litres * 4.186 + 60.0 * 0.49) / ((hot - t) * 4.186)
print(f"about {extra:.1f} L more hot water brings it back to {target:.0f} C")
kwh = share * litres * 4.186 * (hot - cold) / 3600.0
print(f"heating the hot share from {cold:.0f} C took {kwh:.2f} kWh")

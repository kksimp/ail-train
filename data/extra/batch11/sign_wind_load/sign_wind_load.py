signs = [("shop sign", 1.2, 0.8, 3.0), ("road sign", 2.0, 1.5, 2.5), ("billboard", 6.0, 3.0, 5.0)]
def force(s, v):
    return 0.613 * v * v * s[1] * s[2] * 1.8
for v in [20.0, 30.0, 40.0]:
    q = 0.613 * v * v
    print(f"wind {v} m/s ({q:.1f} Pa):")
    for s in signs:
        f = force(s, v)
        m = f * s[3] / 1000.0
        print(f"  {s[0]:<10} {f / 1000.0:>6.2f} kN, base moment {m:>7.2f} kNm")
gust = 0.0
for x in [force(s, 40.0) for s in signs]:
    gust = gust + x
gust = gust / 1000.0
print(f"all three in a 40 m/s gust: {gust:.2f} kN")

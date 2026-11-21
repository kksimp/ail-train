import math
batch = [("tin", 120, 6), ("jar", 220, 4), ("tumbler", 300, 3), ("teacup", 180, 2)]
wax = 0.0
oil = 0.0
candles = 0
for name, ml, count in batch:
    w = float(ml) * 0.86
    o = w * 0.08
    wax += w * float(count)
    oil += o * float(count)
    candles += count
    print(f"{count} x {name:<8} {ml} ml: {w:.1f} g wax + {o:.1f} g oil each")
print(f"{candles} candles: {wax:.1f} g wax ({math.ceil(wax / 1000.0)} bags), {oil:.1f} g fragrance oil")

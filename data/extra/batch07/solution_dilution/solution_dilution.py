S = {"ethanol": 96.0, "bleach": 5.0, "acid": 37.0}
for n, w, v in [("ethanol", 70.0, 500.0), ("bleach", 0.5, 2000.0), ("acid", 10.0, 250.0), ("bleach", 8.0, 100.0), ("ethanol", 40.0, 1000.0)]:
    h = S[n]
    if w > h: print(f"{n} {w:.1f}%: stock is only {h:.1f}%"); continue
    sm = w * v / h; print(f"{n} {w:.1f}% x {v:.0f} ml: {sm:.1f} ml stock + {v - sm:.1f} ml water")

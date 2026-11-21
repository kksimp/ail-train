def blend(a, b, target, batch):
    lo = a if a < b else b
    hi = b if a < b else a
    if target < lo or target > hi:
        return None
    pa = abs(b - target)
    pb = abs(a - target)
    share = pa / (pa + pb)
    return [batch * share, batch * (1.0 - share)]
jobs = [("single cream from double cream and milk", 48.0, 3.5, 18.0, 10.0), ("ice cream base from cream and milk", 36.0, 3.5, 12.0, 4.0), ("half-fat milk from whole and skim", 3.5, 0.1, 1.7, 20.0), ("syrup 30% from 65% and water", 65.0, 0.0, 30.0, 2.0), ("cream at 60% fat", 48.0, 3.5, 60.0, 1.0)]
for name, a, b, t, batch in jobs:
    parts = blend(a, b, t, batch)
    if parts is not None:
        print(f"{name}: {parts[0]:.2f} L of {a}% + {parts[1]:.2f} L of {b}% = {batch} L")
    else:
        print(f"{name}: impossible, the target is outside {b}% to {a}%")

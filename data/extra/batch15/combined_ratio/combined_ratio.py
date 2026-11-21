def pct(a, b): return float(a) / float(b) * 100.0
lines = [("motor", 48200, 37900, 12100, 2900), ("home", 31500, 17400, 9800, 1600), ("liability", 12800, 10700, 3300, 2400), ("travel", 6100, 2300, 2900, 100)]
for name, prem, losses, exps, inv in lines:
    loss = pct(losses, prem); exp = pct(exps, prem)
    combined = loss + exp
    uw = prem - losses - exps
    operating = combined - pct(inv, prem)
    print(f"{name:<9} loss {loss:>5.1f}% + expense {exp:>5.1f}% = {combined:>5.1f}%, underwriting {uw:>6}, operating ratio {operating:.1f}%")
p = sum(l[1] for l in lines)
c = sum(l[2] + l[3] for l in lines)
print(f"company combined ratio {pct(c, p):.1f}%")

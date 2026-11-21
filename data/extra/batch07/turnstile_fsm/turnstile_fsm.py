def st(g, e):
    if e == "fault": return "Broken"
    if g == "Broken": return "Locked" if e == "repair" else "Broken"
    if g == "Locked": return "Unlocked" if e == "coin" else "Locked"
    return "Locked" if e == "push" else "Unlocked"
g = "Locked"; p = b = t = 0
for e in ["push", "coin", "push", "coin", "coin", "push", "push", "fault", "coin", "repair", "coin", "push"]:
    bf = g; g = st(g, e)
    if e == "coin" and bf != "Broken": t += 1
    if e == "push" and bf == "Unlocked": p += 1
    if e == "push" and bf == "Locked": b += 1
    print(f"{e:<6} Gate.{bf} -> Gate.{g}")
print(f"{p} through, {b} blocked pushes, {t} coins kept")

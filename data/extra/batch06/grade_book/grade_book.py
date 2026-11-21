def rs(c, m, f):
    k = (c * 30 + m * 20 + f * 50 + 50) // 100
    if f < 40 and k > 40: return 40, "capped"
    return k, "distinction" if k >= 70 else "merit" if k >= 55 else "pass" if k >= 40 else "fail"
for n, c, m, f in [("Ali", 82, 75, 71), ("Bri", 65, 58, 49), ("Cas", 90, 88, 35), ("Dov", 41, 39, 38), ("Eun", 55, 70, 61)]: k, b = rs(c, m, f); print(f"{n}: {c}/{m}/{f} -> {k} {b}")

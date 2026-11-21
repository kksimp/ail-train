changes = [("petrol", 1.5, 1.65, 1000.0, 970.0), ("cinema ticket", 10.0, 12.0, 500.0, 380.0), ("bread", 1.2, 1.4, 300.0, 285.0), ("coffee to go", 3.0, 3.3, 200.0, 170.0)]
def elasticity(c):
    dq = (c[4] - c[3]) / ((c[3] + c[4]) / 2.0)
    dp = (c[2] - c[1]) / ((c[1] + c[2]) / 2.0)
    return dq / dp
def kind(e):
    m = abs(e)
    return "elastic" if m > 1.0 else ("inelastic" if m < 1.0 else "unit elastic")
for c in changes:
    e = elasticity(c)
    before = c[1] * c[3]
    after = c[2] * c[4]
    print(f"{c[0]:<13} E {e:>6.2f} ({kind(e)}), revenue {before:.2f} -> {after:.2f}")
paid = [ch[0] for ch in changes if ch[2] * ch[4] > ch[1] * ch[3]]
joined = ", ".join(paid)
print(f"price rises that raised revenue: {joined}")

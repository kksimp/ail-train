classes = [("young urban", 1850.0, 296, 1036000.0), ("young rural", 1200.0, 132, 409200.0), ("adult urban", 6400.0, 512, 1638400.0), ("adult rural", 5100.0, 255, 739500.0), ("senior", 2300.0, 161, 547400.0)]
fixed = 45.0; variable = 0.15; profit = 0.05
for name, exp, claims, losses in classes:
    freq = float(claims) / exp
    severity = losses / float(claims)
    pure = freq * severity
    gross = (pure + fixed) / (1.0 - variable - profit)
    print(f"{name:<12} frequency {freq:.3f}, severity {severity:>7.2f}, pure {pure:>6.2f}, gross {gross:>7.2f}")
c = min(classes, key=lambda c: int(c[3] / c[1] * 100.0))
print(f"lowest expected loss: {c[0]}")

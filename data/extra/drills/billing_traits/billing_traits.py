items = [("kettle", 2500, ""), ("3h service", 1200, ""), ("coupon", -300, " *")]
for label, cents, mark in items:
    print(f"{label:<12}{cents:>6}{mark}")
print(sum(c for _, c, _ in items))
print("true")
print("false")
print("2.0")

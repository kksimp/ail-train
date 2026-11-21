print("price   call profit   put profit   straddle")
for pr in [35.0, 40.0, 45.0, 50.0, 55.0, 60.0, 65.0]:
    c = max(pr - 50.0, 0.0) - 3.5; p = max(50.0 - pr, 0.0) - 2.25
    print(f"{pr:>5.0f} {c:>13.2f} {p:>12.2f} {c + p:>10.2f}")
print(f"call breaks even at {50.0 + 3.5:.2f}, put at {50.0 - 2.25:.2f}")

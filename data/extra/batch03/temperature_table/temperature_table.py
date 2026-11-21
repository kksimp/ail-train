print("     C       F       K")
c = -40.0
while c <= 100.0:
    print(f"{c:>6.1f} {c * 9.0 / 5.0 + 32.0:>7.1f} {c + 273.15:>7.2f}"); c += 20.0
print(f"C equals F at {-32.0 / (9.0 / 5.0 - 1.0)}")
print(f"body temperature 37.0 C is {37.0 * 9.0 / 5.0 + 32.0:.1f} F")

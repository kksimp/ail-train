c = "4729"; w = 0; lk = 0
for a in ["1111", "4729", "4720", "0000", "9999", "4729", "4729", "4729", "1234"]:
    if lk > 0: lk -= 1; print(f"{a}: locked ({lk} left)"); continue
    if a == c: w = 0; print(f"{a}: open")
    else:
        w += 1; r = sum(1 for i in range(4) if a[i] == c[i]); print(f"{a}: wrong ({r} digits in place)")
        if w == 3: lk = 2; w = 0; print("  keypad locked")

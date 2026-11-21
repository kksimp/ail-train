fl = [("rectangle 300x400", 300 * 400), ("floor", 200 * 150 // 2), ("rectangle 250x250", 250 * 250)]
t = 0
for l, a in fl:
    c = (a + 9999) // 10000 * 2450; t += c
    print(f"{l} of {a} cm2: {c // 100}.{c % 100:02d}")
print(f"total {t // 100}.{t % 100:02d}")

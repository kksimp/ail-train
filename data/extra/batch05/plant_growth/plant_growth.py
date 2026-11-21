h = 4.0; hw = -1
for w in range(17):
    if w > 0: h = h + 0.45 * h * (1.0 - h / 120.0)
    if w % 2 == 0: print(f"week {w:>2}: {h:>6.1f} cm |{'=' * int(h / 5.0)}")
    if hw < 0 and h >= 60.0: hw = w
print(f"passed half height in week {hw}")

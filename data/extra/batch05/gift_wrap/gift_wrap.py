P = R = 0
for b in ["20x30x10", "15x15x15", "40x5x8", "12x9x30"]:
    l, w, h = sorted(int(x) for x in b.split("x")); a = 2 * (l * w + w * h + h * l) + l * w; r = 2 * (l + w) + l * w * h // 100; P += a; R += r
    print(f"{b}: paper {a} cm2, ribbon {r} cm")
print(f"total paper {P} cm2, ribbon {R} cm")

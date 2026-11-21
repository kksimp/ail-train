def hue(nm):
    if nm < 450.0:
        return "violet"
    elif nm < 495.0:
        return "blue"
    elif nm < 570.0:
        return "green"
    elif nm < 590.0:
        return "yellow"
    elif nm < 620.0:
        return "orange"
    return "red"

def bright(n, t):
    path = 2.0 * n * t
    out = []
    m = 0
    while True:
        lam = path / (float(m) + 0.5)
        if lam < 380.0:
            break
        if lam <= 750.0:
            out.append(lam)
        m += 1
    return out

n = 1.33
for t in [100, 150, 250, 400, 600]:
    waves = bright(n, float(t))
    parts = [f"{w:.0f} nm {hue(w)}" for w in waves]
    shown = "none visible" if not parts else ", ".join(parts)
    print(f"film {t:>3} nm thick: {shown}")
print(f"a film far thinner than the light looks black: {len(bright(n, 20.0))} bright bands at 20 nm")

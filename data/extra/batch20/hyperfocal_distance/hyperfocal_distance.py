def hyperfocal(f, n, coc):
    return f * f / (n * coc) + f

def near(s, h, f):
    return s * (h - f) / (h + s - 2.0 * f)

def far(s, h, f):
    if s >= h:
        return None
    return s * (h - f) / (h - s)

coc = 0.03
subject = 3000.0
for f in [24.0, 50.0, 85.0]:
    for n in [2.8, 8.0]:
        h = hyperfocal(f, n, coc)
        nr = near(subject, h, f) / 1000.0
        v = far(subject, h, f)
        far_text = f"{v / 1000.0:.2f} m" if v is not None else "infinity"
        print(f"{f:.0f} mm f/{n}: hyperfocal {h / 1000.0:.2f} m, sharp from {nr:.2f} m to {far_text}")

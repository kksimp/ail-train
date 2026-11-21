e = 11000000000.0
load = 1200.0
def second_moment(bm, hm):
    b = bm / 1000.0
    h = hm / 1000.0
    return b * h * h * h / 12.0
def sag_mm(w, span, e, i):
    return 5.0 * w * span * span * span * span / (384.0 * e * i) * 1000.0
for bm, hm in [(47.0, 150.0), (47.0, 200.0), (75.0, 225.0)]:
    for span in [3.0, 4.0, 5.0]:
        sag = sag_mm(load, span, e, second_moment(bm, hm))
        limit = span * 1000.0 / 360.0
        verdict = "ok" if sag <= limit else "too bouncy"
        print(f"{bm}x{hm} over {span} m: sag {sag:>5.1f} mm, limit {limit:.1f} mm, {verdict}")

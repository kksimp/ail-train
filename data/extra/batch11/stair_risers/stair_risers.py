def plan(height):
    n = (height + 189) // 190
    riser = float(height) / float(n)
    going = 630.0 - 2.0 * riser
    run = going * float(n - 1)
    ok = riser >= 150.0 and riser <= 220.0 and going >= 220.0 and going <= 300.0
    verdict = "within limits" if ok else "outside limits"
    return f"{n} risers of {riser:.1f} mm, going {going:.1f} mm, run {run / 1000.0:.2f} m, {verdict}"
for name, h in [("cottage", 2400), ("house", 2650), ("office", 3200), ("loft", 2150), ("deck", 600)]:
    print(f"{name:<8} {h} mm: {plan(h)}")

for w, h, g in [(20, 12, 4), (35, 35, 5), (9, 6, 0)]:
    f = 2 * (w + h) - g; s = (f * 10 + 24) // 25; print(f"{w}x{h} m, gate {g} m: {s + 1 if g > 0 else s} posts, {s} spans, {s * 3} rails, {f * 3} m of rail")

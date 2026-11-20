cap, tok, per, last = 3, 3, 250, 0
al = 0
times = [0, 10, 20, 30, 260, 270, 520, 1000, 1001, 1002, 1003, 1004]
for t in times:
    g = (t - last) // per
    if g > 0:
        tok = min(tok + g, cap); last += g * per
    ok = tok > 0
    if ok: tok -= 1; al += 1
    print(f"{t:>5} ms: {'ok' if ok else 'rejected'} ({tok} left)")
print(f"allowed {al} of {len(times)}")

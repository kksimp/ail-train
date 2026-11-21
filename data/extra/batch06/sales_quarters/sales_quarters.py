M = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]; S = [410, 385, 460, 470, 512, 498, 530, 555, 520, 610, 640, 720]; pv = 0
for q in range(4):
    p = S[q * 3:q * 3 + 3]; t = sum(p); b = max(range(3), key=lambda i: (p[i], -i))
    ch = "" if pv == 0 else f" ({(t - pv) * 100 // pv:+}%)"
    print(f"Q{q + 1}: {t}{ch}, best {M[q * 3 + b]}"); pv = t
print(f"year: {sum(S)}")

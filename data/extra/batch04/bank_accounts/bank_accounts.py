b = {"ana": 500, "bo": 120, "cy": 0}
for f, t, a in [("ana", "bo", 200), ("bo", "cy", 400), ("cy", "dee", 10), ("bo", "cy", 300), ("eve", "ana", 5)]:
    if f not in b: print(f"{f} -> {t} {a}: failed, no account {f}"); continue
    if t not in b: print(f"{f} -> {t} {a}: failed, no account {t}"); continue
    if b[f] < a: print(f"{f} -> {t} {a}: failed, {f} is short by {a - b[f]}"); continue
    b[f] -= a; b[t] += a; print(f"{f} -> {t} {a}: done, {b[f]} left")
for k in sorted(b): print(f"{k}: {b[k]}")

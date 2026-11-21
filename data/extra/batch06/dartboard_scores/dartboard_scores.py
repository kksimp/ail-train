T = []
for n in range(1, 21): T += [(n, f"S{n}"), (2 * n, f"D{n}"), (3 * n, f"T{n}")]
T += [(25, "SB"), (50, "DB")]; D = [t for t in T if t[1].startswith("D")]
for g in [40, 81, 121, 170]:
    f = next((d[1] for d in D if d[0] == g), "")
    if not f: f = next((f"{a[1]} {d[1]}" for a in T for d in D if a[0] + d[0] == g), "")
    if not f: f = next((f"{a[1]} {b[1]} {d[1]}" for a in T for b in T for d in D if a[0] + b[0] + d[0] == g), "")
    print(f"{g}: {f or 'no checkout'}")

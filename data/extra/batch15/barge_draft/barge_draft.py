def draft(b, rho): return b[2] / (rho * b[0] * b[1])
def max_cargo(b, rho, limit): return (limit * rho * b[0] * b[1] - b[2]) / 1000.0
b = [40.0, 8.5, 120000.0]
fresh = 1000.0; sea = 1025.0
print(f"empty: river {draft(b, fresh):.3f} m, sea {draft(b, sea):.3f} m")
for t in [100.0, 150.0, 200.0, 150.0]:
    b[2] += t * 1000.0
    flag = " over the limit" if draft(b, fresh) > 2.0 else ""
    print(f"+{t:.0f} t: total {b[2] / 1000.0:.0f} t, river {draft(b, fresh):.3f} m, sea {draft(b, sea):.3f} m{flag}")
e = [40.0, 8.5, 120000.0]
print(f"cargo limit at 2.0 m: river {max_cargo(e, fresh, 2.0):.0f} t, sea {max_cargo(e, sea, 2.0):.0f} t")

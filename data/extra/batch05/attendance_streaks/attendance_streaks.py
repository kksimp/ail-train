def lr(m):
    b = r = 0
    for c in m:
        if c == "P": r += 1; b = max(b, r)
        else: r = 0
    return b
low = []
for n, m in [("Ada", "PPPPPPPAPPPPPPP"), ("Ben", "PPAPPAPPPPAPPPP"), ("Cal", "PPPPPPPPPPPPPPP"), ("Dee", "APPPPPPPPPPPPPA"), ("Eve", "PPPPAAAPPPPPPPP")]:
    p = m.count("P") * 100 // len(m); print(f"{n}: {p}% present, longest streak {lr(m)}")
    if p < 90: low.append(n)
print(f"under 90%: {', '.join(low)}")

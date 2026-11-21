reg = {"Ade": "PPPPAPPPPPPPPPP", "Bel": "PAPAPPAPPPAPPAP", "Cyd": "PPPPPPPPPPPPPPP", "Dee": "AAPPPPAPPPPPPAA"}
def lr(m, w):
    b = c = 0
    for x in m:
        c = c + 1 if x == w else 0; b = max(b, c)
    return b
low = []
for n, m in reg.items():
    p = m.count("P") * 100 // len(m)
    print(f"{n}: {p:>3}% present, best run {lr(m, 'P')}, longest absence {lr(m, 'A')}")
    if p < 80: low.append(n)
print("below 80%: " + ", ".join(low))

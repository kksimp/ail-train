def lab(o): return f"{o[1]}% off" if o[0] == "p" else f"buy {o[1] - 1} get 1 free" if o[0] == "f" else f"{o[2] // 100} off over {o[1] // 100}"
def sav(o, P):
    if o[0] == "p": return sum(P) * o[1] // 100
    if o[0] == "f": return sum(sorted(P)[:len(P) // o[1]])
    return o[2] if sum(P) >= o[1] else 0
O = [("p", 15), ("f", 3), ("m", 5000, 800)]
for B in [[1299, 899, 450, 2100], [599, 599, 599], [4500, 300, 250, 180, 999, 120]]:
    t = sum(B); b = ""; bs = -1
    for o in O:
        s = sav(o, B)
        if s > bs: bs = s; b = lab(o)
    print(f"basket {t // 100}.{t % 100:02}: best is {b}, saving {bs // 100}.{bs % 100:02}")

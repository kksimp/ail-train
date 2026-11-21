def cut_one_way(across, along):
    return (across + 399) // 400 * along

def cut_for(w, l):
    return min(cut_one_way(w, l), cut_one_way(l, w))

def metres(cm):
    return f"{cm // 100}.{cm % 100:02d} m"

rooms = [("lounge", 520, 380), ("bedroom", 360, 330), ("hall", 900, 110), ("dining", 450, 420), ("study", 280, 250)]
total = 0
waste = 0
for name, w, l in rooms:
    cut = cut_for(w, l)
    total += cut
    spare = cut * 400 - w * l
    waste += spare
    seams = (w + 399) // 400 - 1 if cut_one_way(w, l) <= cut_one_way(l, w) else (l + 399) // 400 - 1
    print(f"{name:<8} {w}x{l} cm: cut {metres(cut)}, {seams} seams, waste {spare // 10000}.{spare % 10000 // 100:02d} m2")
cost = total * 98
print(f"roll length {metres(total)}, cost {cost // 100}.{cost % 100:02d}")
print(f"total waste {waste // 10000}.{waste % 10000 // 100:02d} m2")

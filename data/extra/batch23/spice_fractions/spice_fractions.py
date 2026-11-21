class Good:
    def __init__(self, name, value, kilos):
        self.name = name
        self.value = value
        self.kilos = kilos

goods = [Good("saffron", 120, 2), Good("vanilla", 150, 5), Good("pepper", 60, 6), Good("cinnamon", 90, 9), Good("cumin", 40, 8)]
cap = 15
order = sorted(goods, key=lambda g: -(float(g.value) / float(g.kilos)))
room = cap
total = 0.0
for g in order:
    if room == 0:
        break
    take = min(room, g.kilos)
    part = float(g.value) * float(take) / float(g.kilos)
    total += part
    room -= take
    print(f"{g.name:<9} {take:>2} of {g.kilos} kg -> {part:>6.2f}")
print(f"split goods, {cap} kg bag: {total:.2f}")
whole = 0
left = cap
for g in order:
    if g.kilos <= left:
        whole += g.value
        left -= g.kilos
best = 0
for mask in range(32):
    v = 0
    w = 0
    for i in range(5):
        if ((mask >> i) & 1) == 1:
            v += goods[i].value
            w += goods[i].kilos
    if w <= cap and v > best:
        best = v
print(f"whole goods only: greedy {whole}, best possible {best}")

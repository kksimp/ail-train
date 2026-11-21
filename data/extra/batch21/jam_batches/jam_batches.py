fruit = [("strawberry", 6500, 750), ("blackcurrant", 3000, 1000), ("plum", 9200, 600), ("raspberry", 2400, 800)]
jars = sugar_total = boils = 0
for name, g, r in fruit:
    sugar = g * r // 1000
    st = (g + sugar) * 85 // 100
    n = st // 340
    jars += n
    sugar_total += sugar
    b = (g + 3999) // 4000
    boils += b
    print(f"{name:<12} {g} g + {sugar} g sugar, {b} boils: {n} jars and a {st % 340} g pot")
print(f"{jars} jars from {boils} boils; buy {(sugar_total + 999) // 1000} kg bags of sugar")

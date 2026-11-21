def per_layer(c):
    a = (1200 // c[1]) * (800 // c[2])
    b = (1200 // c[2]) * (800 // c[1])
    return max(a, b)
cartons = [("tins", 400, 300, 220, 14), ("cereal", 380, 260, 300, 6), ("tiles", 600, 300, 120, 28), ("bottles", 330, 250, 280, 17)]
for c in cartons:
    layer = per_layer(c)
    layers = (1500 - 150) // c[3]
    count = layer * layers
    limit = "height"
    if count * c[4] > 1000:
        count = 1000 // c[4]; limit = "weight"
    fill = count * c[1] * c[2] * c[3] // 1000000
    print(f"{c[0]:<8} {layer:>2} per layer x {layers} layers -> {count:>3} cartons ({count * c[4]} kg), limited by {limit}, {fill} litres of carton")

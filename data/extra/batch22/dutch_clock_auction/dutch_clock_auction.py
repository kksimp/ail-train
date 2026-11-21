buyers = [["Ana", 71, 30, False], ["Bo", 66, 50, False], ["Cy", 66, 40, False], ["Di", 57, 20, False], ["Ed", 50, 60, False]]
left = 150
price = 90
tick = 0
revenue = 0
while left > 0 and price > 0:
    pick = -1
    for i, b in enumerate(buyers):
        if not b[3] and b[1] >= price and pick == -1:
            pick = i
    if pick == -1:
        price -= 2
        tick += 1
        continue
    boxes = min(buyers[pick][2], left)
    buyers[pick][3] = True
    left -= boxes
    revenue += boxes * price
    print(f"tick {tick:>2}: clock at {price}, {buyers[pick][0]} takes {boxes} boxes, {left} left")
print(f"revenue {revenue}, average {revenue // 150} a box")

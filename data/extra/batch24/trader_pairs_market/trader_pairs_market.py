buyers = [["B1", 95, False], ["B2", 80, False], ["B3", 72, False], ["B4", 68, False], ["B5", 52, False], ["B6", 40, False]]
sellers = [["S1", 30, False], ["S2", 58, False], ["S3", 85, False], ["S4", 66, False], ["S5", 70, False], ["S6", 45, False]]
prices = []
for r in range(6):
    deals = 0
    for i in range(6):
        j = (i + r) % 6
        if not buyers[i][2] and not sellers[j][2] and buyers[i][1] >= sellers[j][1]:
            price = (buyers[i][1] + sellers[j][1]) // 2
            buyers[i][2] = True; sellers[j][2] = True
            prices.append(price); deals += 1
            print(f"round {r + 1}: {buyers[i][0]} buys from {sellers[j][0]} at {price}")
    if deals == 0:
        print(f"round {r + 1}: no deal")
left = [b[0] for b in buyers if not b[2]]
mean = sum(prices) / len(prices)
print(f"{len(prices)} trades, mean price {mean:.2f}, buyers left out: {', '.join(left)}")

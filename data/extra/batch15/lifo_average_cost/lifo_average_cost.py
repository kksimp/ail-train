layers = [(200, 1000), (300, 1080), (250, 1150), (150, 1240)]
def lifo(layers, sold):
    left = sold; cogs = 0; i = len(layers) - 1
    while left > 0 and i >= 0:
        take = layers[i][0] if layers[i][0] < left else left
        cogs += take * layers[i][1]
        left -= take; i -= 1
    return cogs
sold = 620; price = 1600
units = sum(l[0] for l in layers)
spend = sum(l[0] * l[1] for l in layers)
print(f"{units} units bought for {spend} cents, {sold} sold at {price} cents")
revenue = sold * price
l_cogs = lifo(layers, sold)
avg = spend * 100 // units
a_cogs = sold * avg // 100
for name, cogs in [("LIFO", l_cogs), ("average", a_cogs)]:
    print(f"{name:<8} cost of sales {cogs:>7}, gross profit {revenue - cogs:>7}, closing {spend - cogs:>6}")
print(f"average unit cost {avg // 100}.{avg % 100:02} cents")

def charm(c):
    if c < 1000:
        return (c + 10) // 10 * 10 - 1
    if c < 10000:
        return (c + 100) // 100 * 100 - 1
    return (c + 1000) // 1000 * 1000 - 1

def money(c):
    return f"{c // 100}.{c % 100:02d}"

items = [("pencil", 85), ("mug", 412), ("scarf", 1180), ("lamp", 4450), ("kettle", 7385), ("chair", 9420)]
uplift = 0
for name, cost in items:
    plain = cost * 135 // 100
    shelf = charm(plain)
    uplift += shelf - plain
    print(f"{name:<7} cost {money(cost):>6}, cost-plus {money(plain):>6}, shelf {money(shelf):>6}")
print(f"charm endings add {money(uplift)} across the range")

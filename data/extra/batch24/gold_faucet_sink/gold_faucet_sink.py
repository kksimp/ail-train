def simulate(tax_pct):
    players = 200
    supply = players * 100
    each = []
    for day in range(1, 61):
        supply += 40 * players
        supply -= 15 * players
        supply -= supply // 10 * tax_pct // 100
        if day % 10 == 0: each.append(supply // players)
    return each
low = simulate(20); high = simulate(50)
print("day   20% tax         50% tax")
for i in range(6):
    sl = 50 * low[i] // 100; sh = 50 * high[i] // 100
    print(f"{(i + 1) * 10:>3}  {low[i]:>5} each, sword {sl:>4}  {high[i]:>5} each, sword {sh:>4}")
print(f"balance points: {25 * 1000 // 20} and {25 * 1000 // 50} gold per player")

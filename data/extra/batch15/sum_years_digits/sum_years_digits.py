def schedule(cost, salvage, life):
    base = cost - salvage
    digits = life * (life + 1) // 2
    out = []; used = 0
    for k in range(1, life + 1):
        amount = base - used if k == life else base * (life - k + 1) // digits
        used += amount
        out.append(amount)
    return out
cost = 64000; salvage = 4000; life = 6
years = schedule(cost, salvage, life)
print(f"machine cost {cost}, salvage {salvage}, life {life} years, digits {life * (life + 1) // 2}")
book = cost; total = 0
for i, d in enumerate(years):
    book -= d; total += d
    share = d * 100 // (cost - salvage)
    print(f"year {i + 1}: {d:>6} ({share}% of base), book value {book:>6}")
print(f"total depreciation {total}, first two years {years[0] + years[1]}")

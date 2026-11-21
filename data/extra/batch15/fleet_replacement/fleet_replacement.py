price = 90000
resale = [64000, 50000, 40000, 32000, 26000, 21000, 17000, 14000]
upkeep = [3000, 4500, 6500, 9000, 12000, 15500, 19500, 24000]
spent = 0; best_year = 0; best_cost = 1000000
for i in range(len(resale)):
    n = i + 1
    spent += upkeep[i]
    total = price - resale[i] + spent
    avg = total // n
    if avg < best_cost:
        best_cost = avg; best_year = n
    print(f"keep {n} years: total {total:>6}, average {avg:>5} a year {'#' * (avg // 2000)}")
print(f"replace every {best_year} years (average {best_cost} a year)")

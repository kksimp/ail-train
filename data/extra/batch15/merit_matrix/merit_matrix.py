def band(salary, mid):
    r = salary * 100 // mid
    return 0 if r < 90 else 1 if r <= 110 else 2
matrix = [[0, 0, 0], [100, 50, 0], [350, 250, 150], [550, 400, 250], [750, 550, 350]]
people = [("Asha", 41000, 48000, 4), ("Bruno", 52000, 48000, 3), ("Cara", 61000, 60000, 5), ("Dev", 70500, 60000, 2), ("Elin", 39500, 48000, 3), ("Femi", 66000, 60000, 4)]
spend = 0; payroll = 0
for name, sal, mid, rating in people:
    b = band(sal, mid)
    bp = matrix[rating - 1][b]
    rise = sal * bp // 10000
    spend += rise; payroll += sal
    compa = sal * 100 // mid
    print(f"{name:<6} rating {rating}, compa {compa}%: rise {bp // 100}.{bp % 100:02}% = {rise}, new salary {sal + rise}")
pool = payroll * 350 // 10000
print(f"rises {spend} against a pool of {pool}: {'within budget' if spend <= pool else 'over budget'}")

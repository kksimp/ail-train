def half_weeks(age, years):
    total = 0; a = age
    for k in range(min(years, 20)):
        worked = a - 1
        total += 3 if worked >= 41 else 2 if worked >= 22 else 1
        a -= 1
    return total
cap = 700
workers = [("Gwen", 58, 26, 820), ("Hal", 35, 9, 610), ("Ivy", 24, 5, 450), ("Jon", 45, 8, 690), ("Kim", 30, 1, 520)]
for name, age, years, weekly in workers:
    if years < 2:
        print(f"{name:<5} {years} year: not yet eligible"); continue
    hw = half_weeks(age, years)
    pay = min(weekly, cap)
    amount = hw * pay // 2
    print(f"{name:<5} age {age}, {years:>2} years: {hw // 2}.{hw % 2 * 5} weeks x {pay} = {amount}")

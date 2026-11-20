def band(age):
    if age <= 11: return "Child"
    if age <= 17: return "Youth"
    if age >= 65: return "Senior"
    return "Adult"
PRICE = {"Child": 20, "Youth": 32, "Adult": 45, "Senior": 30}
def pass_price(age, days):
    base = PRICE[band(age)] * days
    off = 20 if days >= 6 else 10 if days >= 3 else 0
    return base - base * off // 100
group = [("Ines", 42, 3), ("Tom", 9, 3), ("Ola", 70, 6), ("Raf", 16, 1), ("Uma", 12, 7)]
total = 0
for name, age, days in group:
    p = pass_price(age, days)
    total += p
    print(f"{name:<5} {band(age):<7}{days} days {p:>4}")
print(f"group total: {total}")
print(" ".join(f"{b}={PRICE[b]}" for b in ["Child", "Youth", "Adult", "Senior"]))

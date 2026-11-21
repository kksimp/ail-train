def money(c): return f"{c // 100}.{c % 100:02}"
plan = {"ded": 150000, "pct": 20, "oop": 500000, "paid": 0, "toward": 0}
def claim(bill):
    patient = 0
    left = plan["ded"] - plan["toward"]
    in_ded = bill if bill < left else left
    patient += in_ded
    plan["toward"] += in_ded
    patient += (bill - in_ded) * plan["pct"] // 100
    room = plan["oop"] - plan["paid"]
    if patient > room: patient = room
    plan["paid"] += patient
    return patient
bills = [("GP visit", 18000), ("MRI scan", 120000), ("physio", 45000), ("surgery", 1850000), ("follow-up", 22000), ("rehab", 300000)]
ins = 0
for name, bill in bills:
    p = claim(bill)
    ins += bill - p
    print(f"{name:<10} bill {money(bill):>9}: patient {money(p):>8}, insurer {money(bill - p):>9}, patient so far {money(plan['paid'])}")
print(f"year: patient {money(plan['paid'])}, insurer {money(ins)}")

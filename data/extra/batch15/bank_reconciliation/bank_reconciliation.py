def money(c):
    sign = "-" if c < 0 else ""
    a = abs(c)
    return f"{sign}{a // 100}.{a % 100:02}"
bank = 1284550; books = 1195075
items = [("InTransit", 182000), ("Unpresented", 64500), ("Unpresented", 213025), ("Charge", 2450), ("Interest", 1200), ("Bounced", 4800)]
ab = bank; ak = books
for k, c in items:
    if k == "InTransit": ab += c
    elif k == "Unpresented": ab -= c
    elif k == "Charge": ak -= c
    elif k == "Interest": ak += c
    else: ak -= c
    label = {"InTransit": "deposit in transit: bank +", "Unpresented": "unpresented cheque: bank -", "Charge": "bank charge: books -", "Interest": "interest: books +", "Bounced": "bounced cheque: books -"}[k]
    print(f"  {label}{money(c)}")
print(f"bank statement {money(bank)} -> adjusted {money(ab)}")
print(f"cash book      {money(books)} -> adjusted {money(ak)}")
diff = ab - ak
print("reconciled" if diff == 0 else f"difference {money(diff)} to find")

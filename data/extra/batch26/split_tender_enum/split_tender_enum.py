def money(c): return f"{c // 100}.{c % 100:02}"
def label(t):
    if t[0] == "card": return f"card ..{t[1]}"
    if t[0] == "cash": return "cash"
    return f"voucher {t[1]}"
def settle(total, ts):
    paid = sum(t[-1] for t in ts)
    cash = sum(t[-1] for t in ts if t[0] == "cash")
    names = " and ".join(label(t) for t in ts)
    if paid < total:
        print(f"{money(total)} by {names}: short {money(total - paid)}"); return
    change = min(paid - total, cash)
    lost = paid - total - change
    print(f"{money(total)} by {names}: change {money(change)}, forfeited {money(lost)}")
settle(2350, [("card", "4412", 2000), ("cash", 500)])
settle(1800, [("voucher", "GIFT20", 2000)])
settle(4200, [("voucher", "GIFT10", 1000), ("card", "9031", 3000)])
settle(990, [("cash", 2000)])
settle(1500, [("voucher", "GIFT5", 500), ("cash", 1200)])

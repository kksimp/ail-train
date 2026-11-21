def ratio(a, b): return float(a) / float(b)
def report(name, s):
    current = s["cash"] + s["receivables"] + s["inventory"] + s["prepaid"]
    quick = s["cash"] + s["receivables"]
    liab = s["payables"] + s["short loans"]
    debt = liab + s["long loans"]
    cr = ratio(current, liab)
    flag = "  (may struggle to pay bills)" if cr < 1.0 else ""
    print(f"{name}: current {cr:.2f}, quick {ratio(quick, liab):.2f}, cash {ratio(s['cash'], liab):.2f}, debt/equity {ratio(debt, s['equity']):.2f}{flag}")
shop = {"cash": 18000, "receivables": 4000, "inventory": 61000, "prepaid": 3000, "payables": 52000, "short loans": 20000, "long loans": 40000, "equity": 55000}
agency = {"cash": 42000, "receivables": 88000, "inventory": 0, "prepaid": 6000, "payables": 31000, "short loans": 10000, "long loans": 15000, "equity": 120000}
report("toy shop", shop)
report("design agency", agency)
for k in ["inventory", "receivables"]:
    print(f"{k}: shop {shop[k]}, agency {agency[k]}")

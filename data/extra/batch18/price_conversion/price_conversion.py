menu = {"flat white": 340, "croissant": 285, "porridge": 450, "tea": 220, "brownie": 310}
def show(c): return f"{c // 100}.{c % 100:02}"
eu = {k: (v * 117 + 50) // 100 for k, v in menu.items()}
for k, p in menu.items(): print(f"{k:<11} {show(p):>5} GBP {show(eu[k]):>5} EUR")
o = ["flat white", "croissant", "tea", "tea"]
g = sum(menu[i] for i in o); e = sum(eu[i] for i in o)
print(f"order: {show(g)} GBP or {show(e)} EUR")
print(f"converting the total instead gives {show((g * 117 + 50) // 100)} EUR")

menu = {"soup": 650, "risotto": 1450, "steak": 2400, "tart": 780}
served = {k: v + v // 8 for k, v in menu.items()}
lunch = {k: (v - v // 5 if k in ("risotto", "steak") else v) for k, v in menu.items()}
m = lambda c: f"{c // 100}.{c % 100:02}"
print("item      menu  +12.5%   lunch")
for k, v in menu.items():
    print(f"{k:<8}{m(v):>6}{m(served[k]):>8}{m(lunch[k]):>8}")
t = ["soup", "steak", "steak", "tart"]
print(f"table of four: {m(sum(served[x] for x in t))} with service, {m(sum(lunch[x] for x in t))} at lunch")

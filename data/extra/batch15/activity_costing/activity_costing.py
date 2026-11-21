pools = [("setups", 60000.0, 300.0), ("inspections", 40000.0, 800.0), ("machine hours", 150000.0, 12000.0)]
products = [("standard chair", 5000.0, 9000.0, [60.0, 200.0, 9000.0]), ("custom chair", 400.0, 1000.0, [240.0, 600.0, 3000.0])]
for p in pools:
    print(f"{p[0]:<13} rate {p[1] / p[2]:.2f} per driver unit")
total_oh = 0.0
for p in pools: total_oh = total_oh + p[1]
labour = 0.0
for p in products: labour = labour + p[2]
for prod in products:
    abc = 0.0
    for i in range(len(pools)):
        abc += prod[3][i] * pools[i][1] / pools[i][2]
    old = total_oh * prod[2] / labour
    print(f"{prod[0]}: by labour {old / prod[1]:.2f} per unit, by activity {abc / prod[1]:.2f} per unit")

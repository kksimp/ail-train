returns = [35, -120, 80, 15, -45, 210, -310, 60, -15, 95, -80, 40, -190, 120, 5, -60, 150, -25, 70, -240]
s = sorted(returns)
n = len(s)
position = 1000000
for c in [95, 90, 80]:
    k = n * (100 - c) // 100
    var_bp = -s[k]
    tail = sum(-s[i] for i in range(k))
    es_bp = tail // k
    print(f"{c}%: {k} days beyond, VaR {var_bp} bp = {var_bp * position // 10000}, shortfall {es_bp} bp = {es_bp * position // 10000}")
print(f"worst day {s[0]} bp, best day {s[n - 1]} bp")

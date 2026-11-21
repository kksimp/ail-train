R = [l.split(",") for l in "city,pop_k,area,country\nLeeds,812,552,UK\nLyon,522,48,FR\nGraz,291,128,AT\nTurku,195,246,FI".split("\n")]; H = R[0]; D = R[1:]; tc = []
for c in range(len(H)):
    n = [int(r[c]) for r in D if r[c].isdigit()]
    if len(n) == len(D): print(f"{H[c]}: sum {sum(n)}, min {min(n)}, max {max(n)}")
    else: tc.append(H[c])
print(f"text columns: {', '.join(tc)}")

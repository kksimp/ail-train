def pay_down(order):
    bal = [450000, 120000, 800000, 250000]
    rates = [2199, 2499, 649, 999]
    mins = [9000, 4000, 25000, 6000]
    done = [0, 0, 0, 0]
    months = 0
    interest = 0
    while any(b > 0 for b in bal) and months < 600:
        months += 1
        spare = 60000
        for i in range(4):
            if bal[i] > 0:
                charge = bal[i] * rates[i] // 120000
                interest += charge
                bal[i] += charge
                part = min(mins[i], bal[i])
                bal[i] -= part
                spare -= part
        for i in order:
            part = min(spare, bal[i])
            bal[i] -= part
            spare -= part
        for i in range(4):
            if bal[i] == 0 and done[i] == 0:
                done[i] = months
    return months, interest, done

def money(c):
    return f"{c // 100}.{c % 100:02d}"

names = ["card", "store", "car", "loan"]
B = [450000, 120000, 800000, 250000]
R = [2199, 2499, 649, 999]
M = [9000, 4000, 25000, 6000]
for i in range(4):
    print(f"{names[i]:<5} {money(B[i]):>7} at {R[i] // 100}.{R[i] % 100:02d}%, minimum {money(M[i])}")
for label, order in [("avalanche", [1, 0, 3, 2]), ("snowball", [1, 3, 0, 2])]:
    months, interest, done = pay_down(order)
    joined = ", ".join(f"{names[i]} {done[i]}" for i in order)
    print(f"{label:<9}: debt free in {months} months, interest {money(interest)}; cleared {joined}")

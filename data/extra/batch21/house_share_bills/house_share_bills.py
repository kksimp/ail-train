class Mate:
    def __init__(self, name, a, b):
        self.name, self.moved_in, self.moved_out = name, a, b

def overlap(m, f, t):
    lo = max(m.moved_in, f)
    hi = min(m.moved_out, t)
    return 0 if hi < lo else hi - lo + 1

def split(amount, days):
    total = sum(days)
    shares = [amount * d // total for d in days]
    left = amount - sum(shares)
    order = sorted(range(len(days)), key=lambda i: -((amount * days[i]) % total))
    for i in order:
        if left == 0:
            break
        shares[i] += 1
        left -= 1
    return shares

def money(c):
    return f"{c // 100}.{c % 100:02d}"

mates = [Mate("Rosa", 1, 365), Mate("Tom", 1, 140), Mate("Uma", 60, 365), Mate("Vic", 200, 365)]
bills = [("gas", 1, 90, 41250), ("electric", 91, 181, 30999), ("water", 182, 273, 18800), ("broadband", 274, 365, 12000)]
owed = {}
for what, f, t, amount in bills:
    days = [overlap(m, f, t) for m in mates]
    shares = split(amount, days)
    parts = []
    for i, m in enumerate(mates):
        owed[m.name] = owed.get(m.name, 0) + shares[i]
        parts.append(f"{m.name} {money(shares[i])}")
    print(f"{what:<9} {money(amount):>7}: {', '.join(parts)}")
for name, c in owed.items():
    print(f"{name:<5} owes {money(c):>7} for the year")

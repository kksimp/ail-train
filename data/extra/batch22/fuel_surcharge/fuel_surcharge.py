def surcharge_tenths(price):
    if price <= 140:
        return 0
    return (price - 140) // 3 * 5

def money(c):
    return f"{c // 100}.{c % 100:02d}"

weeks = [(138, 125000), (146, 98000), (152, 143500), (161, 110000), (149, 87500), (171, 132000)]
haul = 0
extra = 0
for i, (price, charge) in enumerate(weeks):
    t = surcharge_tenths(price)
    add = charge * t // 1000
    haul += charge
    extra += add
    print(f"week {i + 1}: diesel {money(price)}, surcharge {t // 10}.{t % 10}%, line haul {money(charge):>8} + {money(add):>6}")
print(f"line haul {money(haul)}, fuel surcharge {money(extra)} ({extra * 1000 // haul // 10}.{extra * 1000 // haul % 10}%)")

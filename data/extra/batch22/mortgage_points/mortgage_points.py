import math

def money(c):
    return f"{c // 100}.{c % 100:02d}"

def payment_cents(loan, yearly, months):
    r = yearly / 12.0
    p = loan * r / (1.0 - (1.0 + r) ** float(-months))
    return int(math.floor(p * 100.0 + 0.5))

def break_even(cost, saving):
    return (cost + saving - 1) // saving

loan = 300000.0
deals = [(0, 650), (1, 625), (2, 600), (3, 580)]
pays = [payment_cents(loan, float(bp) / 10000.0, 360) for _, bp in deals]
for i, (pts, bp) in enumerate(deals):
    cost = pts * 300000
    pay = pays[i]
    seven = cost + pay * 84
    be = "-" if pts == 0 else f"{break_even(cost, pays[0] - pay)} months"
    print(f"points {pts}, rate {bp // 100}.{bp % 100:02d}%: payment {money(pay)}, break-even {be}, 7-year cost {money(seven)}")

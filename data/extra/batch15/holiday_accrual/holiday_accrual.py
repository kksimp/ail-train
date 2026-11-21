def hm(minutes):
    sign = "-" if minutes < 0 else ""
    m = abs(minutes)
    return f"{sign}{m // 60}h{m % 60:02}"
yearly = 25 * 8 * 60
cap = 40 * 60
staff = [("Rosa", 100, [0, 480, 0, 960, 0, 2400, 2400, 0, 480, 0, 960, 1920]), ("Tom", 60, [0, 0, 1440, 0, 0, 1440, 1440, 0, 0, 0, 0, 0]), ("Ines", 80, [480] * 12)]
for name, fte, taken in staff:
    monthly = yearly * fte // 100 // 12
    balance = 0; lowest = 0
    for t in taken:
        balance += monthly - t
        lowest = min(lowest, balance)
    kept = min(balance, cap)
    lost = balance - kept
    print(f"{name:<5} {fte:>3}% FTE accrues {hm(monthly)} a month; year end {hm(balance)}, carried {hm(kept)}, lost {hm(lost)}, lowest {hm(lowest)}")

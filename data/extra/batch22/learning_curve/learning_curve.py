import math

def unit_hours(first, rate, n):
    b = math.log(rate) / math.log(2.0)
    return first * float(n) ** b

for n in [1, 2, 3, 5, 8, 10, 20]:
    a = unit_hours(100.0, 0.8, n)
    b = unit_hours(100.0, 0.9, n)
    print(f"unit {n:>2}: {a:>6.2f} h at 80%, {b:>6.2f} h at 90%")
for pct in [80, 90]:
    rate = float(pct) / 100.0
    total = 0.0
    for n in range(1, 11):
        total += unit_hours(100.0, rate, n)
    avg = total / 10.0
    print(f"{pct}% curve: first 10 units {total:.1f} h, average {avg:.1f} h")

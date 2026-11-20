def cents(c): return f"{c // 100}.{c % 100:02d}"
for price, months in [(120000, 12), (99999, 4), (500, 3), (1000, 0), (-5, 2)]:
    if months <= 0:
        print(f"{cents(abs(price))} over {months}: months must be positive, got {months}"); continue
    if price < 0:
        print(f"{cents(abs(price))} over {months}: price cannot be negative"); continue
    e, r = divmod(price, months)
    pays = [e] * months; pays[0] += r
    bal = price; lines = []
    for i, a in enumerate(pays):
        bal -= a
        if i < 2 or i == len(pays) - 1:
            lines.append(f"m{i + 1} {cents(a)} left {cents(bal)}")
    print(f"{cents(price)} over {months}: {'; '.join(lines)}")

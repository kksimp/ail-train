import re
import sys

lines = sys.stdin.read().splitlines()
toks = lines[0].split() if lines else []
if len(toks) != 4 or not all(re.fullmatch(r"[0-9]+", t) for t in toks):
    print("bad header")
    sys.exit()
stock, reorder, qty, lead = (int(t) for t in toks)
if qty < 1 or lead < 1:
    print("bad header")
    sys.exit()
pending = []  # (arrival day, quantity)
day = sold = lost = orders = 0
for n, raw in enumerate(lines[1:], 2):
    t = raw.strip()
    if not t:
        continue
    if not re.fullmatch(r"-?[0-9]+", t) or int(t) < 0:
        print(f"line {n}: bad demand")
        continue
    demand = int(t)
    day += 1
    for arr, q in pending:
        if arr == day:
            stock += q
            print(f"  received {q}")
    pending = [p for p in pending if p[0] != day]
    take = min(demand, stock)
    stock -= take
    sold += take
    lost += demand - take
    print(f"day {day}: demand {demand} sold {take} lost {demand - take} stock {stock}")
    if stock + sum(q for _, q in pending) <= reorder:
        pending.append((day + lead, qty))
        orders += 1
        print(f"  ordered {qty} arriving day {day + lead}")
print(f"total sold {sold} lost {lost} orders {orders}")
print(f"final stock {stock}")

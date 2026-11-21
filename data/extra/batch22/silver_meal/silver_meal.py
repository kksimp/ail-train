def lot_cost(demand, frm, upto, setup, hold):
    c = setup
    for k in range(frm, upto + 1):
        c += (k - frm) * hold * demand[k]
    return c

def fixed_cost(demand, every, setup, hold):
    total = 0
    i = 0
    while i < len(demand):
        last = min(i + every - 1, len(demand) - 1)
        total += lot_cost(demand, i, last, setup, hold)
        i += every
    return total

demand = [40, 70, 20, 60, 80, 30, 50]
setup = 120
hold = 2
i = 0
total = 0
while i < len(demand):
    end = i
    while end + 1 < len(demand):
        now = lot_cost(demand, i, end, setup, hold)
        more = lot_cost(demand, i, end + 1, setup, hold)
        periods = end - i + 1
        if more * periods < now * (periods + 1):
            end += 1
        else:
            break
    c = lot_cost(demand, i, end, setup, hold)
    q = sum(demand[i:end + 1])
    print(f"period {i + 1}: make {q} for periods {i + 1}-{end + 1}, cost {c}")
    total += c
    i = end + 1
print(f"Silver-Meal {total}, every period {fixed_cost(demand, 1, setup, hold)}, every second period {fixed_cost(demand, 2, setup, hold)}")

def settle(sales, carry_in):
    st = -carry_in
    lt = 0
    for _, held, gain in sales:
        if held > 365:
            lt += gain
        else:
            st += gain
    mixed = st + lt
    if st < 0 and lt > 0:
        if mixed >= 0:
            lt, st = mixed, 0
        else:
            st, lt = mixed, 0
    elif lt < 0 and st > 0:
        if mixed >= 0:
            st, lt = mixed, 0
        else:
            lt, st = mixed, 0
    tax = max(st, 0) * 30 // 100 + max(lt, 0) * 15 // 100
    loss = -(min(st, 0) + min(lt, 0))
    deduct = min(loss, 3000)
    return st, lt, tax, deduct, loss - deduct

years = [[("A", 200, 5000), ("B", 400, -8000), ("C", 90, -2000), ("D", 800, 12000)], [("E", 30, -9000), ("F", 500, 2000), ("G", 100, 1500)], [("H", 60, 4000), ("I", 700, 6000)]]
carry = 0
for i, sales in enumerate(years):
    st, lt, tax, deduct, c = settle(sales, carry)
    print(f"year {i + 1}: short {st:>6}, long {lt:>6}, tax {tax:>5}, deducted {deduct}, carried {c}")
    carry = c

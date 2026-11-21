cost = 42000; residual = 6000; expected = 240000
def charge(km, book):
    raw = (cost - residual) * km // expected
    room = book - residual
    return room if raw > room else raw
usage = [52000, 61000, 38000, 47000, 55000, 20000]
print(f"delivery van: {(cost - residual) * 100 // expected} cents per km over {expected} km")
book = cost
for i, km in enumerate(usage):
    c = charge(km, book)
    book -= c
    note = " (fully written down)" if book == residual else ""
    print(f"year {i + 1}: {km:>6} km, charge {c:>5}, book {book:>5}{note}")
print(f"driven {sum(usage)} km against {expected} expected")

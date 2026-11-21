bal = {"GC-100": 5000, "GC-200": 1200, "GC-300": 8000}; exp = {"GC-300": 40}
kinds = [0, 0, 0]
for code, c in [("GC-100", 1999), ("GC-200", 1500), ("GC-999", 500), ("GC-300", 2500), ("GC-100", 3001), ("GC-200", 1200)]:
    if code not in bal:
        print(f"{code}: refused, unknown card {code}"); kinds[0] += 1; continue
    last = exp.get(code, 9999)
    if 52 > last:
        print(f"{code}: refused, card expired on day {last}"); kinds[1] += 1; continue
    if bal[code] < c:
        print(f"{code}: refused, only {bal[code]} cents left"); kinds[2] += 1; continue
    bal[code] -= c
    print(f"{code}: paid {c}, {bal[code]} left")
print(f"refusals unknown/expired/short: {kinds}")

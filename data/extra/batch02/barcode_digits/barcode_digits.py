def cd(ds): return (10 - sum(d if i % 2 == 0 else d * 3 for i, d in enumerate(ds)) % 10) % 10
def valid(c):
    if not c.isdigit(): return False
    ds = [int(x) for x in c]
    return len(ds) == 13 and cd(ds[:12]) == ds[12]
for c in ["4006381333931", "4006381333932", "9780306406157", "12345", "97803064061x7"]:
    print(f"{c}: {str(valid(c)).lower()}")
for s in ["590123412345", "978014300723", "000000000000"]:
    print(f"{s} -> {s}{cd([int(x) for x in s])}")

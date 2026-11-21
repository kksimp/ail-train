book = [("P-101", 1, 730), ("P-102", 91, 1095), ("P-103", 182, 1460), ("P-104", 274, 900), ("P-105", 335, 1825)]

def earned(p, day):
    used = min(max(day - p[1] + 1, 0), 365)
    return p[2] * used // 365

te = 0
tu = 0
for p in book:
    e = earned(p, 365)
    u = p[2] - e
    te += e
    tu += u
    print(f"{p[0]} from day {p[1]:>3}: premium {p[2]:>4}, earned {e:>4}, unearned {u:>4}")
print(f"year end: earned {te}, unearned reserve {tu}")
p = book[2]
for day in [200, 300]:
    refund = p[2] - earned(p, day)
    short = refund * 90 // 100
    print(f"{p[0]} cancelled on day {day}: pro rata refund {refund}, short-rate {short}")

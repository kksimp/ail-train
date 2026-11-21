import math
def expected_profit(booked, seats, p, fare, bump):
    q = 1.0 - p
    pmf = math.pow(q, float(booked))
    revenue = 0.0; bumped = 0.0
    for k in range(booked + 1):
        flown = k if k < seats else seats
        revenue += pmf * float(flown) * fare
        if k > seats:
            bumped += pmf * float(k - seats)
        pmf = pmf * float(booked - k) / float(k + 1) * p / q
    return [revenue - bumped * bump, bumped]
seats = 180
best = seats; best_value = 0.0
for booked in [180, 184, 188, 192, 196, 200, 204]:
    r = expected_profit(booked, seats, 0.92, 250.0, 800.0)
    print(f"book {booked}: expected bumped {r[1]:.3f}, expected net {r[0]:.0f}")
    if r[0] > best_value:
        best_value = r[0]; best = booked
print(f"best of these: book {best} for {seats} seats")

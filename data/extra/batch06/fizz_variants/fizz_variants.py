def sy(n, R):
    o = "".join(w for d, w in R if n % d == 0); return o or str(n)
for R in [[(3, "Fizz"), (5, "Buzz")], [(2, "Ping"), (7, "Pong")], [(3, "A"), (4, "B"), (6, "C")]]:
    print(" ".join(sy(n, R) for n in range(1, 16)))
    for d, w in R: print(f"  {w}: {sum(1 for n in range(1, 101) if n % d == 0)}")

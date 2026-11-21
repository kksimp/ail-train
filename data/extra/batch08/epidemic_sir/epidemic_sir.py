s = 9990.0; i = 10.0; r = 0.0; pd = 0; pk = 0.0
for day in range(161):
    if day % 20 == 0: print(f"day {day:>3}: S {s:>7.0f}  I {i:>6.0f}  R {r:>7.0f}")
    if i > pk: pk = i; pd = day
    nc = 0.3 * s * i / 10000.0; rc = 0.1 * i; s -= nc; i += nc - rc; r += rc
print(f"peak {pk:.0f} infected on day {pd}; {s:.0f} never infected")

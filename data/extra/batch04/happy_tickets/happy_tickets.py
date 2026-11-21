ds = lambda n: sum(int(c) for c in str(n))
w = [0] * 28
for h in range(1000): w[ds(h)] += 1
print(f"lucky tickets from 000000 to 999999: {sum(x * x for x in w)}")
print(f"most common half sum: {w.index(max(w))} ({max(w)} ways)")
lk = lambda t: ds(t // 1000) == ds(t % 1000)
for t in [123321, 100001, 555555, 123456, 902560]: print(f"{t:06d}: {str(lk(t)).lower()}")
print(f"first lucky ticket after 123456: {next(t for t in range(123457, 124000) if lk(t))}")

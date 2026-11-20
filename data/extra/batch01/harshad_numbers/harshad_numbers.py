def ds(n): return sum(int(c) for c in str(n))
def h(n): return n > 0 and n % ds(n) == 0
print(" ".join(str(n) for n in [n for n in range(1, 200) if h(n)][:15]))
run = best = bs = 0
for n in range(1, 2000):
    if h(n):
        run += 1
        if run > best:
            best, bs = run, n - run + 1
    else:
        run = 0
print(f"longest run below 2000: {best} from {bs}")
print(f"count below 1000: {sum(1 for n in range(1, 1000) if h(n))}")

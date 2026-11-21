def next_perm(xs):
    i = len(xs) - 2
    while i >= 0 and xs[i] >= xs[i + 1]:
        i -= 1
    if i < 0:
        return False
    j = len(xs) - 1
    while xs[j] <= xs[i]:
        j -= 1
    xs[i], xs[j] = xs[j], xs[i]
    xs[i + 1:] = reversed(xs[i + 1:])
    return True

xs = [1, 2, 3]
seen = [str(xs)]
while next_perm(xs):
    seen.append(str(xs))
print(f"orders of 1 2 3: {' '.join(seen)}")
ys = [1, 1, 2, 2]
count = 1
while next_perm(ys):
    count += 1
print(f"distinct orders of 1 1 2 2: {count}")
for n in [534976, 12443322, 4321, 1999]:
    ds = [int(c) for c in str(n)]
    if next_perm(ds):
        print(f"next number after {n} with the same digits: {''.join(str(d) for d in ds)}")
    else:
        print(f"{n} is already the largest with its digits")

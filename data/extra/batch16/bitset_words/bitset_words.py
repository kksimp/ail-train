def make(xs):
    w = [0, 0, 0]
    for x in xs:
        w[x // 60] |= 1 << (x % 60)
    return w

def popcount(x):
    return bin(x).count("1")

def size(w):
    return sum(popcount(x) for x in w)

def members(w):
    return [i for i in range(180) if (w[i // 60] >> (i % 60)) & 1 == 1]

sixes = make([i for i in range(180) if i % 6 == 0])
tens = make([i for i in range(180) if i % 10 == 0])
both = [sixes[k] & tens[k] for k in range(3)]
either = [sixes[k] | tens[k] for k in range(3)]
only6 = [sixes[k] & ~tens[k] for k in range(3)]
print(f"multiples of 6: {size(sixes)}, of 10: {size(tens)}")
print(f"both: {size(both)} -> {members(both)}")
print(f"either: {size(either)}")
print(f"6 but not 10: {size(only6)}, first ones {members(only6)[:6]}")
print(f"word 0 of both in hex: {both[0]:x}")

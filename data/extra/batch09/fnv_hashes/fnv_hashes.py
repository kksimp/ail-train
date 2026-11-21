def fnv1a(s):
    h = 2166136261
    for c in s:
        h = h ^ ord(c)
        h = (h * 16777619) % 4294967296
    return h

def djb2(s):
    h = 5381
    for c in s:
        h = (h * 33 + ord(c)) % 4294967296
    return h

def spread(keys, kind):
    buckets = [0] * 8
    for k in keys:
        h = fnv1a(k) if kind == 0 else djb2(k)
        buckets[h % 8] += 1
    return buckets

for w in ["", "a", "foobar", "hello", "hellp"]:
    print(f"{w:<7} fnv1a {fnv1a(w):08x}  djb2 {djb2(w):08x}")
keys = [f"user{i}" for i in range(24)]
a = spread(keys, 0)
b = spread(keys, 1)
print(f"fnv1a buckets {a}, largest {max(a)}")
print(f"djb2  buckets {b}, largest {max(b)}")

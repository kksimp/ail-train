def gamma(n):
    bits = f"{n:b}"
    return "0" * (len(bits) - 1) + bits

def decode(cs):
    out = []
    i = 0
    while i < len(cs):
        zeros = 0
        while cs[i] == '0':
            zeros += 1
            i += 1
        v = 0
        for k in range(zeros + 1):
            v = v * 2 + int(cs[i + k])
        out.append(v)
        i += zeros + 1
    return out

for n in [1, 2, 3, 4, 5, 9, 17, 100]:
    print(f"{n:>3} -> {gamma(n)}")
gaps = [3, 1, 7, 12, 2, 1, 1, 30]
stream = "".join(gamma(g) for g in gaps)
back = " ".join(str(v) for v in decode(stream))
print(f"stream {stream}")
print(f"{len(stream)} bits for {len(gaps)} gaps, decoded {back}")

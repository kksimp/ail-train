def hex2(b):
    digits = "0123456789ABCDEF"
    return f"%{digits[b // 16]}{digits[b % 16]}"

def encode(s):
    out = []
    for c in s:
        n = ord(c)
        if (c.isalnum() and n < 128) or c in "-_.~":
            out.append(c)
        elif n < 128:
            out.append(hex2(n))
        else:
            out.append(hex2(192 | (n >> 6)))
            out.append(hex2(128 | (n & 63)))
    return "".join(out)

params = [("q", "café & crème"), ("page", "2"), ("sort", "price:asc"), ("tag", "50% off"), ("a", "x/y?z"), ("tag", "new")]
pairs = []
for k, v in params:
    enc = encode(v)
    print(f"{k:<5} {v:<14} -> {enc}")
    pairs.append(f"{encode(k)}={enc}")
canonical = "&".join(sorted(pairs))
print(f"canonical: {canonical}")

def pattern(n, rails):
    out, r, step = [], 0, 1
    for _ in range(n):
        out.append(r)
        if rails > 1:
            if r == 0: step = 1
            elif r == rails - 1: step = -1
            r += step
    return out
def enc(t, rails):
    p = pattern(len(t), rails)
    return "".join(t[i] for r in range(rails) for i in range(len(t)) if p[i] == r)
def dec(t, rails):
    p = pattern(len(t), rails)
    order = [i for r in range(rails) for i in range(len(t)) if p[i] == r]
    out = [" "] * len(t)
    for k, i in enumerate(order):
        out[i] = t[k]
    return "".join(out)
msg = "WEAREDISCOVEREDFLEEATONCE"
for rails in [2, 3, 4]:
    e = enc(msg, rails)
    print(f"{rails} rails: {e} -> {str(dec(e, rails) == msg).lower()}")
print("".join(str(r) for r in pattern(8, 3)))
print(enc("hi", 5))

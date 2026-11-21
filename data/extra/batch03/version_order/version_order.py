def parts(v): return [int(p) for p in v.split(".")]
def cmp(a, b):
    pa, pb = parts(a), parts(b); n = max(len(pa), len(pb))
    pa += [0] * (n - len(pa)); pb += [0] * (n - len(pb))
    return (pa > pb) - (pa < pb)
for a, b in [("1.9", "1.10"), ("2.0", "2"), ("0.2.0", "0.10"), ("3.1.4", "3.1.3")]:
    c = cmp(a, b); print(f"{a} {'<' if c < 0 else '>' if c > 0 else '='} {b}")
print(" ".join(sorted(["1.10.0", "1.2", "1.9.3", "0.9", "1.2.10", "1.2.2", "2.0.0"], key=lambda v: parts(v) + [0] * (4 - len(parts(v))))))

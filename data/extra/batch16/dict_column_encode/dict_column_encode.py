def bit_width(n):
    w = 0
    while n > 0:
        w += 1
        n >>= 1
    return w

column = ["Lima", "Oslo", "Cairo", "Lima", "Perth", "Oslo", "Delhi", "Cairo", "Lima", "Quito", "Oslo", "Perth", "Accra", "Lima"]
d = sorted(set(column))
codes = [d.index(c) for c in column]
width = bit_width(len(d) - 1)
print("dictionary [" + ", ".join(d) + "]")
print(f"codes {codes}, {width} bits each")
raw = sum(len(c) for c in column)
packed = sum(len(c) for c in d) + (len(column) * width + 7) // 8
print(f"raw {raw} bytes, encoded {packed} bytes")
for lo in ["M", "D"]:
    first = len(d)
    for i, x in enumerate(d):
        if first == len(d) and x >= lo:
            first = i
    hits = sum(1 for k in codes if k >= first)
    print(f"city >= {lo}: code >= {first}, {hits} rows")

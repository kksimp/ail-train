def ways(s):
    ds = [int(c) for c in s]
    prev2 = 1
    prev1 = 1 if len(ds) > 0 and ds[0] != 0 else 0
    for i in range(1, len(ds)):
        cur = 0
        if ds[i] != 0:
            cur += prev1
        pair = ds[i - 1] * 10 + ds[i]
        if 10 <= pair <= 26:
            cur += prev2
        prev2 = prev1
        prev1 = cur
    return prev1

def letter(n):
    return chr(64 + n)

def expand(ds, i, sofar, out):
    if i == len(ds):
        out.append(sofar)
        return
    if ds[i] != 0:
        expand(ds, i + 1, sofar + letter(ds[i]), out)
        if i + 1 < len(ds):
            pair = ds[i] * 10 + ds[i + 1]
            if pair <= 26:
                expand(ds, i + 2, sofar + letter(pair), out)

for s in ["12", "226", "1212", "2101", "301", "11106", "1111111111", "2626262626"]:
    print(f"{s:<11} {ways(s)} readings")
for s in ["1212", "2101"]:
    out = []
    ds = [int(c) for c in s]
    expand(ds, 0, "", out)
    shown = " ".join(out)
    print(f"{s}: {shown}")

def ab(a, b):
    x = a[::-1]; y = b[::-1]; o = []; c = 0
    for i in range(max(len(x), len(y))):
        s = (1 if i < len(x) and x[i] == "1" else 0) + (1 if i < len(y) and y[i] == "1" else 0) + c; o.append(str(s % 2)); c = s // 2
    if c: o.append("1")
    return "".join(reversed(o))
def mb(a, b):
    t = "0"; sh = ""
    for c in reversed(b):
        if c == "1": t = ab(t, a + sh)
        sh += "0"
    return t
for a, b in [("1011", "110"), ("1111", "1"), ("100000", "11111"), ("101", "101"), ("0", "1101")]:
    s = ab(a, b); m = mb(a, b); ok = int(s, 2) == int(a, 2) + int(b, 2) and int(m, 2) == int(a, 2) * int(b, 2)
    print(f"{a} + {b} = {s}, {a} x {b} = {m}, checked {'true' if ok else 'false'}")

D = "0123456789abcdefghijklmnopqrstuvwxyz"
def tb(n, b):
    if n == 0: return "0"
    v = abs(n); o = ""
    while v: o = D[v % b] + o; v //= b
    return ("-" if n < 0 else "") + o
for n, b in [(255, 2), (255, 16), (255, 36), (-42, 3), (0, 7), (1000000, 36)]:
    s = tb(n, b); print(f"{n} in base {b}: {s} (back {int(s, b)})")
print("ff in base 16 is 255, 9 in base 8 is -1")

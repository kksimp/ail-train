V = [(1000, "M"), (900, "CM"), (500, "D"), (400, "CD"), (100, "C"), (90, "XC"), (50, "L"), (40, "XL"), (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")]
def rm(n):
    o = ""
    for v, s in V:
        while n >= v: o += s; n -= v
    return o
for y in [1066, 1492, 1888, 1999, 2026]: print(f"{y}: {rm(y)}")
Y = range(1900, 2031); lg = max(Y, key=lambda y: (len(rm(y)), -y)); sl = min(len(rm(y)) for y in Y)
print(f"longest: {lg} {rm(lg)} ({len(rm(lg))} letters)"); print(f"shortest ({sl} letters): " + ", ".join(str(y) for y in Y if len(rm(y)) == sl))

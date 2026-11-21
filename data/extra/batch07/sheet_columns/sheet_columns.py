def tn(c):
    n = 0
    for ch in c: n = n * 26 + ord(ch) - 64
    return n
def tl(n):
    o = []
    while n > 0: n -= 1; o.append(chr(n % 26 + 65)); n //= 26
    return "".join(reversed(o))
for c in ["A", "Z", "AA", "AZ", "BA", "ZZ", "AAA", "XFD"]: n = tn(c); print(f"{c} = {n}, back {tl(n)}")
for c in ["C7", "AB12", "XFD1048576"]:
    l = "".join(x for x in c if x.isalpha()); d = "".join(x for x in c if x.isdigit()); print(f"{c}: row {d}, column {tn(l)}")

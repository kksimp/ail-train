cart = [("kettle", 1, 2999, False), ("kids coat", 2, 1850, True), ("batteries", 4, 325, False), ("car seat", 1, 8900, True)]
def money(c): return f"{c // 100}.{c % 100:02}"
def tot(ls):
    i = n = v = 0
    for _, q, c, r in ls:
        net = q * c; i += q; n += net; v += net * (5 if r else 20) // 100
    return i, n, v
i, n, v = tot(cart)
print(f"{i} items, net {money(n)}, VAT {money(v)}, total {money(n + v)}")
i2, n2, v2 = tot([l for l in cart if l[3]])
print(f"reduced-rate lines: {i2} items, VAT {money(v2)}")
print(f"dearest line: {max(cart, key=lambda l: l[1] * l[2])[0]}")

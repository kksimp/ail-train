import math
symbols = ['A', 'B', 'C', 'D']
counts = [4, 2, 1, 1]
total = 8
cum = [0]
for c in counts:
    cum.append(cum[-1] + c)
msg = "ABACABAD"
low, width, den = 0, 1, 1
for ch in msg:
    k = symbols.index(ch)
    low = low * total + width * cum[k]
    width = width * counts[k]
    den = den * total
print(f"message {msg}: interval [{low}/{den}, {low + width}/{den})")
bits = 1
while True:
    scale = 1 << bits
    m = (low * scale + den - 1) // den
    if m * den < (low + width) * scale:
        break
    bits += 1
code = "".join(str((m >> (bits - 1 - i)) & 1) for i in range(bits))
ent = 0.0
for c in counts:
    p = c / total
    ent -= p * math.log(p) / math.log(2.0)
bound = ent * len(msg)
print(f"code {code}: {bits} bits; entropy bound {bound:.2f} bits, plain 2-bit code {2 * len(msg)} bits")
pn, pd = m, 1 << bits
out = []
for i in range(len(msg)):
    k = 0
    while cum[k + 1] * pd <= pn * total:
        k += 1
    out.append(symbols[k])
    pn = pn * total - cum[k] * pd
    pd = pd * counts[k]
print(f"decoded back: {''.join(out)}")

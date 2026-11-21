UNITS = "αβγδεϛζηθ"
TENS = "ικλμνξοπϙ"
HUNDREDS = "ρστυφχψωϡ"

def letter(s, d):
    return s[d - 1]

def to_greek(n):
    out = []
    th = n // 1000
    if th > 0:
        out.append("͵" + letter(UNITS, th))
    h = n // 100 % 10
    t = n // 10 % 10
    u = n % 10
    if h > 0:
        out.append(letter(HUNDREDS, h))
    if t > 0:
        out.append(letter(TENS, t))
    if u > 0:
        out.append(letter(UNITS, u))
    out.append("ʹ")
    return "".join(out)

def value(s):
    total = 0
    scale = 1
    for c in s:
        if c == '͵':
            scale = 1000
            continue
        v = 0
        if c in UNITS:
            v = UNITS.index(c) + 1
        elif c in TENS:
            v = (TENS.index(c) + 1) * 10
        elif c in HUNDREDS:
            v = (HUNDREDS.index(c) + 1) * 100
        total += v * scale
        scale = 1
    return total

ok = 0
nums = [1, 6, 12, 99, 256, 666, 900, 1821, 2026, 9999]
for n in nums:
    g = to_greek(n)
    back = value(g)
    if back == n:
        ok += 1
    print(f"{n:>5} = {g} (reads back as {back})")
print(f"{ok} of {len(nums)} round trips agree")

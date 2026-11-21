NAMES = ["black", "brown", "red", "orange", "yellow", "green", "blue", "violet", "grey", "white"]

def tolerance(c):
    return {"brown": "1%", "red": "2%", "gold": "5%", "silver": "10%"}.get(c, "20%")

def ohms_text(v):
    if v >= 1000000:
        return f"{v / 1000000.0} Mohm"
    elif v >= 1000:
        return f"{v / 1000.0} kohm"
    return f"{v} ohm"

def decode(bands):
    n = len(bands)
    value = 0
    for b in bands[0:n - 2]:
        if b not in NAMES:
            raise ValueError(f"unknown colour {b}")
        value = value * 10 + NAMES.index(b)
    if bands[n - 2] not in NAMES:
        raise ValueError(f"unknown colour {bands[n - 2]}")
    for _ in range(NAMES.index(bands[n - 2])):
        value *= 10
    return ohms_text(value)

def encode(v):
    m = 0
    x = v
    while x >= 100:
        x //= 10
        m += 1
    return [NAMES[x // 10], NAMES[x % 10], NAMES[m], "gold"]

codes = [["yellow", "violet", "red", "gold"], ["brown", "black", "orange", "silver"], ["orange", "orange", "brown", "gold"], ["brown", "green", "black", "red", "brown"], ["red", "pink", "red", "gold"]]
for c in codes:
    shown = "-".join(c)
    try:
        v = decode(c)
        print(f"{shown}: {v} {tolerance(c[-1])}")
    except ValueError as err:
        print(f"{shown}: {err}")
for v in [220, 4700, 100000, 1500000]:
    print(f"{ohms_text(v)} is {'-'.join(encode(v))}")

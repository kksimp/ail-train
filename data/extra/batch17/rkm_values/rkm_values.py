def milliohms(code):
    mults = {'R': 1000, 'K': 1000000, 'M': 1000000000}
    cs = list(code.upper())
    at = -1
    for i, c in enumerate(cs):
        if c in mults:
            if at >= 0:
                return None, f"two multiplier letters in {code}"
            at = i
        elif not c.isdigit():
            return None, f"bad character in {code}"
    if at < 0:
        return None, f"no multiplier letter in {code}"
    w = "".join(cs[:at])
    whole = int(w) if w != "" else 0
    frac_text = "".join(cs[at + 1:])
    mult = mults[cs[at]]
    value = whole * mult
    scale = mult // 10
    for c in frac_text:
        value += int(c) * scale
        scale = scale // 10
    return value, None

def show(m):
    if m >= 1000000000:
        return f"{m // 1000000000}.{m % 1000000000 // 10000000:02} MΩ"
    if m >= 1000000:
        return f"{m // 1000000}.{m % 1000000 // 10000:02} kΩ"
    return f"{m // 1000}.{m % 1000 // 10:02} Ω"

for code in ["4K7", "R47", "2M2", "100R", "1K0", "68K", "0R1", "4K7K", "12", "5X1"]:
    v, err = milliohms(code)
    if v is not None:
        print(f"{code:<5} {show(v)}")
    else:
        print(f"{code:<5} error: {err}")

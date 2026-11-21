def keypad(c):
    table = "22233344455566677778889999"
    up = c.upper()
    if up.isalpha():
        return table[ord(up) - 65]
    return c

def to_e164(raw):
    body = raw
    ext = ""
    low = raw.lower()
    at = low.find("ext")
    if at >= 0:
        ext = raw[at + 3:].strip()
        if ext.startswith("."):
            ext = ext[1:]
        ext = ext.strip()
        body = raw[:at]
    digits = []
    plus = body.strip().startswith("+")
    for c in body:
        k = keypad(c)
        if k.isdigit():
            digits.append(k)
    num = "".join(digits)
    if not plus and num.startswith("00"):
        plus = True
        num = num[2:]
    if not plus:
        if len(num) == 11 and num.startswith("1"):
            num = num[1:]
        if len(num) != 10:
            return None, f"{len(num)} digits is not a full number"
        num = "1" + num
    if len(num) < 8 or len(num) > 15:
        return None, f"bad length {len(num)}"
    tail = "" if ext == "" else f" x{ext}"
    return f"+{num}{tail}", None

inputs = ["(555) 010-4477", "+44 20 7946 0958", "0044 20 7946 0958", "555-0104", "1-800-FLOWERS", "+1 (555) 010-4477 ext. 12", "555.010.4477", "+12"]
for raw in inputs:
    v, err = to_e164(raw)
    if v is not None:
        print(f"{raw:<26} {v}")
    else:
        print(f"{raw:<26} rejected: {err}")

def parse(text):
    t = text.lower()
    parts = t.split("e")
    mant = parts[0]
    exp = int(parts[1].replace("+", "")) if len(parts) > 1 else 0
    negative = mant.startswith("-")
    if negative:
        mant = mant[1:]
    dot = mant.find(".")
    if dot < 0:
        dot = len(mant)
    whole = mant.replace(".", "")
    lead = 0
    while lead < len(whole) - 1 and whole[lead] == '0':
        lead += 1
    digits = whole[lead:]
    return (negative, digits, exp + dot - 1 - lead)

def normal(s):
    negative, digits, exp = s
    sign = "-" if negative else ""
    rest = "." + digits[1:] if len(digits) > 1 else ""
    return f"{sign}{digits[0:1]}{rest} x 10^{exp}"

def plain(s):
    negative, digits, exp = s
    sign = "-" if negative else ""
    point = exp + 1
    if point <= 0:
        return f"{sign}0." + "0" * (-point) + digits
    if point >= len(digits):
        return sign + digits + "0" * (point - len(digits))
    return f"{sign}{digits[:point]}.{digits[point:]}"

for text in ["6.022e23", "-1.5E-3", "42", "3.00e+08", "0.000250", "1234.5", "9.81"]:
    s = parse(text)
    print(f"{text:<10} {normal(s):<20} {plain(s):<26} {len(s[1])} sig figs")

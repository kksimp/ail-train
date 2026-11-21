def to_int(s):
    t = s[1:] if s.startswith("-") else s
    return int(s) if t.isdigit() and t != "" else None

def parse_amount(raw, hint):
    s = raw.replace(" ", "").replace("'", "")
    last_dot = s.rfind(".")
    last_comma = s.rfind(",")
    decimal = ""
    if last_dot >= 0 and last_comma >= 0:
        decimal = "." if last_dot > last_comma else ","
    elif last_dot >= 0 or last_comma >= 0:
        mark = "." if last_dot >= 0 else ","
        at = max(last_dot, last_comma)
        after = len(s) - at - 1
        if s.count(mark) > 1:
            decimal = ""
        elif after == 3:
            decimal = hint
        else:
            decimal = mark
    whole = s
    frac = ""
    if decimal != "" and decimal in s:
        at = s.rfind(decimal)
        whole = s[:at]
        frac = s[at + 1:]
    digits = whole.replace(".", "").replace(",", "")
    n = to_int(digits)
    if n is None:
        return "unreadable"
    f = to_int(frac)
    if f is None:
        f = 0
    return f"{n} + {f}/10^{len(frac)}"

inputs = ["1.234,56", "1,234.56", "1 234,5", "1'234.75", "12,5", "1.234.567", "2,500", "2.500", "0,99", "12x"]
for raw in inputs:
    us = parse_amount(raw, ",")
    eu = parse_amount(raw, ".")
    note = "" if us == eu else "  (ambiguous)"
    print(f"{raw:<10} en: {us:<18} de: {eu}{note}")

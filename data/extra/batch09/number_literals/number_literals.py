def digit_value(c):
    if c.isdigit():
        return int(c)
    if c.isalpha():
        return ord(c.lower()) - 87
    return 99

def read_literal(text):
    cs = list(text)
    sign = 1
    if len(cs) > 0 and cs[0] == '-':
        sign = -1
        cs = cs[1:]
    base = 10
    if len(cs) >= 2 and cs[0] == '0' and cs[1] in "xob":
        base = 16 if cs[1] == 'x' else (8 if cs[1] == 'o' else 2)
        cs = cs[2:]
    if not cs:
        return None, "no digits"
    if cs[0] == '_' or cs[-1] == '_':
        return None, "underscore at an end"
    value = 0
    prev = ' '
    for c in cs:
        if c == '_':
            if prev == '_':
                return None, "double underscore"
        else:
            d = digit_value(c)
            if d >= base:
                return None, f"'{c}' is not a base {base} digit"
            value = value * base + d
        prev = c
    return sign * value, None

for lit in ["42", "-17", "0x1F", "0xff_ff", "0o755", "0b1010_0101", "1_000_000", "0x", "12ab", "1__0", "0b102", "_5"]:
    v, err = read_literal(lit)
    if v is not None:
        print(f"{lit:<12} = {v}")
    else:
        print(f"{lit:<12} error: {err}")

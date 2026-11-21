def shape(s):
    return "".join('9' if c.isdigit() else 'A' if c.isalpha() else '?' for c in s)

def format_code(country, raw):
    s = raw.upper().replace(" ", "").replace("-", "")
    sh = shape(s)
    if country == "UK":
        ok = sh in ["A99AA", "A999AA", "AA99AA", "AA999AA", "A9A9AA", "AA9A9AA"]
        return f"{s[:len(s) - 3]} {s[len(s) - 3:]}" if ok else "invalid"
    if country == "US":
        return s if sh == "99999" else f"{s[:5]}-{s[5:]}" if sh == "999999999" else "invalid"
    if country == "CA":
        return f"{s[:3]} {s[3:]}" if sh == "A9A9A9" else "invalid"
    if country == "NL":
        return f"{s[:4]} {s[4:]}" if sh == "9999AA" and not s.startswith("0") else "invalid"
    return "unknown country"

codes = [("UK", "sw1a1aa"), ("UK", "M1 1AE"), ("UK", "EC1A 1BB"), ("UK", "12345"), ("US", "90210"), ("US", "10001-0001"), ("US", "9021"), ("CA", "k1a0b1"), ("CA", "K1A-0B"), ("NL", "1012ab"), ("NL", "0123 AB"), ("FR", "75001")]
good = 0
for country, raw in codes:
    out = format_code(country, raw)
    if out != "invalid" and out != "unknown country":
        good += 1
    print(f"{country} {raw:<11} -> {out}")
print(f"{good} of {len(codes)} valid")

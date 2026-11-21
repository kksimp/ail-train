def unit_bytes(u):
    return {"": 1, "b": 1, "k": 1000, "kb": 1000, "m": 1000000, "mb": 1000000, "g": 1000000000, "gb": 1000000000, "t": 1000000000000, "tb": 1000000000000, "kib": 1024, "mib": 1048576, "gib": 1073741824, "tib": 1099511627776}.get(u.lower(), -1)

def parse_size(s):
    t = s.replace(" ", "")
    i = 0
    while i < len(t) and (t[i].isdigit() or t[i] == '.'):
        i += 1
    number = t[:i]
    mult = unit_bytes(t[i:])
    if mult < 0 or number == "":
        return None, f"cannot read '{s}'"
    parts = number.split(".")
    whole = int(parts[0]) if parts[0] != "" else 0
    total = whole * mult
    if len(parts) > 1:
        frac = parts[1]
        den = 10 ** len(frac)
        total += (int(frac) if frac != "" else 0) * mult // den
    return total, None

quota = 1099511627776
uses = [("photos", "1.5GB"), ("mail", "512 MiB"), ("notes", "750k"), ("backups", "0.25TiB"), ("music", "3.2 GiB"), ("odd", "12 parsecs")]
used = 0
for name, text in uses:
    b, err = parse_size(text)
    if b is not None:
        used += b
        print(f"{name:<8} {text:>10} = {b:>15,} bytes")
    else:
        print(f"{name:<8} {text:>10}   {err}")
left = quota - used
verdict = "within" if left >= 0 else "over"
print(f"used {used:,} of {quota:,} bytes: {verdict} quota by {abs(left):,}")

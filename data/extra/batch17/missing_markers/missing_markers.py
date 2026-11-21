def to_int(s):
    t = s[1:] if s.startswith("-") else s
    return int(s) if t.isdigit() and t != "" else None

def is_marker(low):
    return low in ["", "na", "n/a", "-", "?"]

def clean(raw):
    s = raw.strip()
    low = s.lower()
    if is_marker(low):
        return None
    return to_int(s.replace(",", ""))

column = ["1,234", " 56 ", "NA", "n/a", "-", "", "789", "1,000", "?", "12", "4x", " 2,500"]
present = []
missing = 0
bad = []
for raw in column:
    low = raw.strip().lower()
    v = clean(raw)
    if v is not None:
        present.append(v)
    elif is_marker(low):
        missing += 1
    else:
        bad.append(raw)
sorted_vals = sorted(present)
median = sorted_vals[len(sorted_vals) // 2]
bad_s = "[" + ", ".join(bad) + "]"
print(f"parsed {len(present)}, missing {missing}, unreadable {len(bad)}: {bad_s}")
print(f"sorted: {sorted_vals}")
print(f"median used for gaps: {median}")
filled = [clean(r) if clean(r) is not None else median for r in column]
print(f"filled: {filled}")
print(f"sum after filling: {sum(filled)}")

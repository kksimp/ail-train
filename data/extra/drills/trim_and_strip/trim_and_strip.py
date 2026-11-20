def strip_prefix(s, p):
    return s[len(p):] if s.startswith(p) else None

def strip_suffix(s, p):
    return s[:len(s) - len(p)] if s.endswith(p) else None

def clean_key(raw):
    t = raw.strip()
    n = strip_prefix(t, "export ")
    return (t if n is None else n).rstrip()

def clean_value(raw):
    t = raw.strip()
    n = strip_suffix(t, ";")
    n = t if n is None else n
    i = strip_prefix(n, '"')
    i = n if i is None else i
    o = strip_suffix(i, '"')
    return i if o is None else o

lines = ['  export PATH = "/usr/bin";  ', "name=  ale  ", "export   depth =3;", "   # a comment", "broken line"]
for line in lines:
    if line.lstrip().startswith("#"):
        print(f"comment [{line.lstrip()}]")
        continue
    parts = line.split("=", 1)
    if len(parts) != 2:
        print(f"skip [{line.rstrip()}]")
        continue
    print(f"{clean_key(parts[0])} -> [{clean_value(parts[1])}]")
print(f"[{'  both  '.lstrip()}] [{'  both  '.rstrip()}] [{'  both  '.strip()}]")
print(strip_suffix("x.ail", ".ail") or "no suffix")
print(strip_suffix("x.txt", ".ail") or "no suffix")

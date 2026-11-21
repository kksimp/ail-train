def count_endings(cs):
    crlf = 0
    lf = 0
    cr = 0
    i = 0
    while i < len(cs):
        c = ord(cs[i])
        if c == 13 and i + 1 < len(cs) and ord(cs[i + 1]) == 10:
            crlf += 1
            i += 2
            continue
        if c == 13:
            cr += 1
        elif c == 10:
            lf += 1
        i += 1
    return [crlf, lf, cr]

def to_lf(cs):
    out = []
    i = 0
    while i < len(cs):
        c = cs[i]
        if ord(c) == 13:
            out.append('\n')
            if i + 1 < len(cs) and ord(cs[i + 1]) == 10:
                i += 1
        else:
            out.append(c)
        i += 1
    return "".join(out)

cr = chr(13)
text = f"name,qty{cr}\napple,3{cr}\npear,5\nplum,2{cr}fig,9{cr}\n"
cs = list(text)
k = count_endings(cs)
names = ["CRLF", "LF", "CR"]
for i in range(3):
    print(f"{names[i]:<4} {k[i]}")
best = 0
for i in range(1, 3):
    if k[i] > k[best]:
        best = i
mixed = "true" if len([x for x in k if x > 0]) > 1 else "false"
print(f"dominant: {names[best]}, mixed: {mixed}")
fixed = to_lf(cs)
rows = fixed.rstrip().split("\n")
print(f"after: {len(rows)} lines, {len(fixed)} chars (was {len(text)})")
for r in rows:
    print(f"  {r}")

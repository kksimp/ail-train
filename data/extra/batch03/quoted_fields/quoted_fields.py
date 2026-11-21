def fields(line):
    out, cur, q, i = [], "", False, 0
    while i < len(line):
        c = line[i]
        if q:
            if c == '"':
                if i + 1 < len(line) and line[i + 1] == '"': cur += '"'; i += 1
                else: q = False
            else: cur += c
        elif c == '"': q = True
        elif c == ',': out.append(cur); cur = ""
        else: cur += c
        i += 1
    out.append(cur)
    return out
for l in ['plain,three,fields', '"Smith, Jo",42,"likes ""tea"""', 'a,,c,', '"",x']:
    f = fields(l); print(f"{len(f)}: " + " ".join(f"[{x}]" for x in f))

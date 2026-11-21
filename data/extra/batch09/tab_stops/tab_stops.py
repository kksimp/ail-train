def expand_tabs(line, stop):
    out = []
    for c in line:
        if c == '\t':
            out.append(' ')
            while len(out) % stop != 0:
                out.append(' ')
        else:
            out.append(c)
    return "".join(out)

def entab_lead(line, stop):
    spaces = 0
    for c in line:
        if c != ' ':
            break
        spaces += 1
    return "\\t" * (spaces // stop) + " " * (spaces % stop) + line[spaces:]

rows = ["name\tqty\tprice", "tea\t4\t2.50", "biscuits\t12\t1.20", "a\tbb\tccc\tdddd"]
for stop in [8, 4]:
    print(f"tab stops every {stop}:")
    for r in rows:
        print(f"  {expand_tabs(r, stop)}|")
for line in ["        indented twice", "      six spaces", "   three"]:
    print(entab_lead(line, 4))

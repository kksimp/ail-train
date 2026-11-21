def escape_field(s):
    out = []
    for c in s:
        if c == '\\':
            out.append("\\\\")
        elif c == '\n':
            out.append("\\n")
        elif ord(c) == 9:
            out.append("\\t")
        else:
            out.append(c)
    return "".join(out)

def unescape_field(s, tab):
    cs = list(s)
    out = []
    i = 0
    while i < len(cs):
        if cs[i] == '\\' and i + 1 < len(cs):
            nc = cs[i + 1]
            piece = "\n" if nc == 'n' else tab if nc == 't' else "\\" if nc == '\\' else "\\" + nc
            out.append(piece)
            i += 2
        else:
            out.append(cs[i])
            i += 1
    return "".join(out)

tab = chr(9)
rows = [["id", "note", "path"], ["1", "line one\nline two", "C:\\temp"], ["2", "tab" + tab + "inside", "plain"], ["3", "", "a\\nb"]]
all_ok = True
for row in rows:
    line = tab.join(escape_field(f) for f in row)
    print(line.replace(tab, " | "))
    back = [unescape_field(f, tab) for f in line.split(tab)]
    if back != row:
        all_ok = False
        print("  mismatch!")
print(f"rows: {len(rows)}, round trip ok: {'true' if all_ok else 'false'}")

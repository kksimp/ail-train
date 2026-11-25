import sys

lines = sys.stdin.read().split("\n")
if lines and lines[-1] == "":
    lines.pop()
if lines:
    toks = lines[0].split(" ")
    widths = []
    ok = True
    for t in toks:
        if t.isdigit() and t.isascii() and int(t) > 0:
            widths.append(int(t))
        else:
            ok = False
    if not ok:
        print("error: bad widths")
    else:
        for rec in lines[1:]:
            if rec == "":
                continue
            pos = 0
            out = []
            for w in widths:
                f = rec[pos:pos + w].strip(" ")
                pos += w
                if "," in f or '"' in f:
                    f = '"' + f.replace('"', '""') + '"'
                out.append(f)
            print(",".join(out))

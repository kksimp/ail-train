def inline(s):
    cs = list(s)
    out = []
    i = 0
    while i < len(cs):
        c = cs[i]
        if c == '*' or c == '_' or c == '`':
            i += 1
        elif c == '[':
            rest = s[i:]
            mid = rest.find("](")
            endp = rest.find(")")
            if mid > 0 and endp > mid:
                out.append(rest[1:mid])
                out.append(" <")
                out.append(rest[mid + 2:endp])
                out.append(">")
                i += endp + 1
            else:
                out.append("[")
                i += 1
        else:
            out.append(c)
            i += 1
    return "".join(out)

def convert(line):
    if line.startswith("## "):
        text = inline(line[3:])
        return [text, "-" * len(text)]
    if line.startswith("# "):
        text = inline(line[2:]).upper()
        return [text, "=" * len(text)]
    if line.startswith("- "):
        return ["  * " + inline(line[2:])]
    if line.startswith("> "):
        return ["  | " + inline(line[2:])]
    if line == "---":
        return ["~" * 20]
    return [inline(line)]

doc = ["# Release notes", "Version **2.1** is *out* now.", "## Fixes", "- crash on [empty files](https://ex.com/1)", "- slow `grep` on big logs", "1. update the app", "2. restart it", "> back up your settings first", "---", "Thanks to __everyone__ who reported bugs."]
count = 0
for line in doc:
    for out in convert(line):
        print(out)
        count += 1
print(f"{len(doc)} markdown lines -> {count} text lines")

def opens(prev):
    return prev in " ([—\n"

def curl(text):
    t = text.replace("---", "—").replace("--", "–").replace("...", "…")
    out = []
    prev = ' '
    for c in t:
        if c == '"':
            out.append('“' if opens(prev) else '”')
        elif c == "'":
            out.append('‘' if opens(prev) else '’')
        else:
            out.append(c)
        prev = c
    return "".join(out)

lines = ["\"It's late,\" she said.", "The 'old' house---empty now---stood by the road.", "Pages 12--19 cover the '80s... mostly.", "He called it \"the best (and 'only') option.\"", "Don't stop; we're nearly there."]
changed = 0
for l in lines:
    c = curl(l)
    changed += len([ch for ch in c if ch in "“”‘’—–…"])
    print(c)
print(f"{changed} typographic characters put in")

def sc(t):
    out, start = [], True
    for c in t:
        if c.isalpha():
            out.append(c.upper() if start else c.lower())
            start = False
        else:
            out.append(c)
            if c in ".!?":
                start = True
    return "".join(out)
def loud(t):
    ls = [c for c in t if c.isalpha()]
    return len(ls) > 0 and sum(1 for c in ls if c.isupper()) * 2 > len(ls)
for l in ["HELLO THERE. HOW ARE YOU?", "this is fine! really. ok", "ALREADY Fine.", "42 is THE answer. yes"]:
    print(f"[{'loud' if loud(l) else 'calm'}] {sc(l)}")

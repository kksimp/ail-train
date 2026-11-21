def sq(s, only):
    out = []
    for c in s:
        if not out or out[-1] != c:
            out.append(c)
        elif only is not None and c not in only:
            out.append(c)
    return "".join(out)
for t in ["aaabccddddde", "too    many     spaces  here", "Mississippi", "", "zzz"]:
    a = sq(t, None); s = sq(t, {" "})
    print(f"'{a}' (-{len(t) - len(a)}) | '{s}'")

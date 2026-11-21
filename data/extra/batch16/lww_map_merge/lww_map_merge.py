def merge(a, b):
    out = dict(a)
    for k, e in b.items():
        if k in out:
            cur = out[k]
            if (e[0], e[1]) > (cur[0], cur[1]):
                out[k] = e
        else:
            out[k] = e
    return out

def render(m):
    return " ".join(f"{k}={m[k][2]}" for k in sorted(m) if m[k][2] != "")

a = {"theme": (5, "a", "dark"), "lang": (2, "a", "en"), "font": (7, "a", "mono")}
b = {"theme": (6, "b", "light"), "lang": (2, "b", "de"), "zoom": (3, "b", "110")}
c = {"font": (9, "c", ""), "zoom": (4, "c", "125"), "theme": (6, "a", "sepia")}
print(f"a: {render(a)}")
print(f"b: {render(b)}")
print(f"c: {render(c)}")
one = merge(merge(a, b), c)
two = merge(merge(c, a), b)
three = merge(b, merge(c, a))
print(f"(a+b)+c: {render(one)}")
print(f"(c+a)+b: {render(two)}")
print(f"b+(c+a): {render(three)}")
same = "true" if render(one) == render(two) and render(two) == render(three) else "false"
print(f"all orders agree: {same}")

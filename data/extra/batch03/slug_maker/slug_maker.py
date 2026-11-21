def slug(t):
    out = ""; p = False
    for c in t.lower():
        if c.isascii() and c.isalnum():
            if p and out: out += "-"
            p = False; out += c
        else: p = True
    return out
for t in ["Hello, World!", "  AIL 0.2: What's new?  ", "C++ & Rust -- a comparison", "100% Pure", "---", "Already-a-slug"]:
    print(f'"{t}" -> "{slug(t)}"')

def m(c):
    if c.islower(): return chr(219 - ord(c))
    if c.isupper(): return chr(155 - ord(c))
    return c
def at(t):
    return "".join(m(c) for c in t)
for t in ["Hello, World!", "wizard", "Atbash 2024", "zyx ABC"]:
    e = at(t)
    print(f"{t} -> {e} -> {at(e)}")
print("mirror-reverse words: " + ", ".join(w for w in ["wizard", "hold", "glow", "bevy", "girt"] if at(w) == w[::-1]))

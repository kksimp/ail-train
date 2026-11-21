def ck(n, e, a, p):
    if not n.strip(): return None, "name is empty"
    if "@" not in e: return None, "email has no @"
    at = e.index("@")
    if at == 0 or "." not in e[at:]: return None, f"email {e} looks wrong"
    try: ag = int(a)
    except ValueError: return None, f"age {a} is not a number"
    if ag < 13: return None, "must be 13 or over"
    if len(p) < 8: return None, "password shorter than 8"
    if not any(c.isdigit() for c in p): return None, "password needs a digit"
    return f"welcome, {n.strip()} ({ag})", None
for f in [("Asha", "asha@example.org", "29", "tulips2024"), ("", "x@y.z", "20", "abcdefgh1"), ("Ben", "ben.example.org", "31", "password9"), ("Cleo", "cleo@site", "40", "longpass1"), ("Dan", "dan@mail.net", "twelve", "secret123"), ("Eve", "eve@mail.net", "11", "letmein22"), ("Fay", "fay@mail.net", "35", "short1"), ("Gus", "gus@mail.net", "50", "nodigitshere")]:
    m, e = ck(*f); print(f"ok: {m}" if m else f"rejected: {e}")

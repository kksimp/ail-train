sm = ["of", "and", "the", "for", "in", "a", "on"]
def ac(p):
    ws = [w for w in p.replace("-", " ").split(" ") if w]
    return "".join(w[0].upper() for i, w in enumerate(ws) if i == 0 or w.lower() not in sm)
for p in ["portable network graphics", "Bank of the North", "the end of the line", "first-in first-out", "  as  soon as   possible "]:
    print(f"{ac(p):<6} {p.strip()}")

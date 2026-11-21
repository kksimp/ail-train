t = "   The  Quick   Brown Fox Jumps Over   "
print(f'start:   "{t}"')
for n, f in [("trim", str.strip), ("squeeze", lambda s: " ".join(w for w in s.split(" ") if w)), ("lower", str.lower), ("dashes", lambda s: s.replace(" ", "-")), ("shorten", lambda s: s[:20] if len(s) > 20 else s)]:
    t = f(t); print(f'{n:<8} "{t}"')

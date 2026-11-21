for s in ["hello world", "  spaced   out  text ", "", "ALL CAPS HERE", "o"]:
    ws = [w for w in s.split(" ") if w]
    print(f'"{s}": {len(ws)} words, "{" ".join(w[0].upper() + w[1:].lower() for w in ws)}"')

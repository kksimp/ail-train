def pattern(word):
    seen = {}
    out = []
    for c in word:
        if c not in seen:
            seen[c] = chr(65 + len(seen))
        out.append(seen[c])
    return "".join(out)

dictionary = ["that", "high", "eyes", "noon", "deed", "puppy", "hello", "sees", "boot", "test", "teeth", "added", "level", "radar", "tooth", "otto", "abba", "attic"]
groups = {}
for w in dictionary:
    groups.setdefault(pattern(w), []).append(w)
for p, ws in groups.items():
    if len(ws) > 1:
        print(f"{p:<6} " + " ".join(ws))
for secret in ["XQQX", "RKJRK", "MZZMJ", "WLXW"]:
    lower = secret.lower()
    p = pattern(lower)
    matches = groups.get(p, [])
    shown = "no word" if not matches else ", ".join(matches)
    print(f"cipher {secret} ({p}) could be: {shown}")

V = {"name": "Rosa", "day": "Friday", "time": "10:30", "room": "B2"}
def fill(t):
    out = ""; miss = []; i = 0
    while i < len(t):
        if t[i] == "<":
            j = t.find(">", i + 1)
            if j >= 0:
                n = t[i + 1:j]
                if n in V: out += V[n]
                else:
                    out += f"<{n}>"
                    if n not in miss: miss.append(n)
                i = j + 1; continue
        out += t[i]; i += 1
    return out, miss
for t in ["Hi <name>, see you <day> at <time>.", "Room <room>, bring <item> and <item>.", "No placeholders here.", "Broken <name"]:
    o, m = fill(t); print(o)
    if m: print("  missing: [" + ", ".join(f'"{x}"' for x in m) + "]")

L = set("acelnrt")
def sc(w): return (1 if len(w) == 4 else len(w)) + (7 if L <= set(w) else 0)
t = 0
for w in ["central", "rental", "learn", "cat", "nectar", "trace", "clean", "plant", "eel", "react", "lance", "cantle", "tea", "teal"]:
    if len(w) < 4 or "e" not in w or not set(w) <= L: continue
    s = sc(w); t += s; print(f"{w}: {s}")
print(f"total {t}")

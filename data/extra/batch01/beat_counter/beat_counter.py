def sound(b):
    a, c = b % 3, b % 4
    if a == 0 and c == 0: return "KICK+SNARE"
    if a == 0: return "kick"
    if c == 0: return "snare"
    return "."
line = []
t = {}
for b in range(1, 25):
    s = sound(b)
    line.append(s if s == "." else s[0])
    t[s] = t.get(s, 0) + 1
for i in range(0, 24, 8):
    print(" ".join(line[i:i + 8]))
for name in ["kick", "snare", "KICK+SNARE", "."]:
    print(f"{name:>10}: {t.get(name, 0)}")

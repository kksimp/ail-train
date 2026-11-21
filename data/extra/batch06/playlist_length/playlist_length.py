def sc(t): m, s = t.split(":"); return int(m) * 60 + int(s)
def ms(s): return f"{s // 60}:{s % 60:02}"
T = [("Intro", "1:12"), ("Northern", "4:35"), ("Glass", "3:58"), ("Echoes", "6:41"), ("Tide", "5:03"), ("Lantern", "3:27"), ("Ridge", "7:15"), ("Coda", "2:50")]
print(f"total {ms(sum(sc(t[1]) for t in T))}"); sd = 1; u = 0; n = []
for nm, d in T:
    s = sc(d)
    if u + s > 22 * 60: print(f"side {sd} ({ms(u)}): {', '.join(n)}"); sd += 1; u = 0; n = []
    u += s; n.append(nm)
print(f"side {sd} ({ms(u)}): {', '.join(n)}")

family = [("Dad", 450, 15), ("Mum", 480, 20), ("Zoe", 465, 25), ("Kai", 495, 10), ("Gran", 570, 30)]

def hhmm(t):
    return f"{t // 60:02d}:{t % 60:02d}"

order = sorted(family, key=lambda p: -p[1])
slots = []
limit = 24 * 60
for p in order:
    finish = min(limit, p[1] - 10)
    start = finish - p[2]
    slots.append([family.index(p), start, finish])
    limit = start
slots = sorted(slots, key=lambda s: s[1])
for s in slots:
    p = family[s[0]]
    print(f"{hhmm(s[1])}-{hhmm(s[2])} {p[0]:<5} leaves {hhmm(p[1])} ({p[1] - s[2]} min to spare)")
print(f"first alarm: {family[slots[0][0]][0]} at {hhmm(slots[0][1] - 5)}")

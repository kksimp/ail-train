THRESHOLDS = [0, 300, 900, 2700, 6500, 14000, 23000, 34000]

def level(xp):
    return sum(1 for t in THRESHOLDS if xp >= t)

names = ["Aldo", "Bree", "Cass", "Dunn"]
xp = [0, 250, 0, 800]
sessions = [[450, 1100], [1850, 2400], [3200, 1500], [5600, 4400]]
for s, session in enumerate(sessions):
    present = [True, s != 1, True, s != 2]
    earned = sum(session)
    crowd = sum(1 for p in present if p)
    share = earned // crowd
    ups = []
    for i in range(4):
        if present[i]:
            before = level(xp[i])
            xp[i] += share
            after = level(xp[i])
            if after > before:
                ups.append(f"{names[i]} to {after}")
    news = "no level ups" if not ups else ", ".join(ups)
    print(f"session {s + 1}: {earned} xp / {crowd} = {share} each; {news}")
for i in range(4):
    nxt = THRESHOLDS[level(xp[i])] - xp[i] if level(xp[i]) < len(THRESHOLDS) else 0
    print(f"{names[i]:<5} level {level(xp[i])}, {xp[i]:>5} xp, {nxt} to next")

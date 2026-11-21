S = [(0, 15.0), (6, 20.0), (9, 16.0), (17, 21.0), (22, 15.0)]; t = 15.0; hh = 0
for h in range(24):
    tg = [s[1] for s in S if h >= s[0]][-1]; ht = t < tg
    if ht: t += 1.5; hh += 1
    else: t -= 0.5
    if h % 3 == 0: print(f"{h:02}:00 target {tg:.1f} heat {'on' if ht else 'off':<3} room {t:.1f}")
print(f"heating ran {hh} hours")

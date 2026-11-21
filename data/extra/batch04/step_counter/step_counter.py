D = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]; ld = ""; lt = 0
for w, s in [("Rae", [8200, 10400, 9100, 12050, 7600, 15300, 4300]), ("Sol", [11000, 10100, 9900, 10020, 10800, 6000, 13400]), ("Tam", [5400, 6100, 7200, 6600, 8800, 9900, 10001])]:
    t = sum(s); b = max(range(7), key=lambda i: s[i]); m = [D[i] for i in range(7) if s[i] >= 10000]
    print(f"{w}: {t:,} steps, best {D[b]}, goal met {len(m)}x ({' '.join(m)})")
    if t > lt: lt = t; ld = w
print(f"leader: {ld}")

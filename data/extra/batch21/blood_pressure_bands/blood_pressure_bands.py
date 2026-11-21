names = ["Normal", "Elevated", "Stage1", "Stage2", "Crisis"]

def sys_rank(s):
    return 4 if s > 180 else 3 if s >= 140 else 2 if s >= 130 else 1 if s >= 120 else 0

def dia_rank(d):
    return 4 if d > 120 else 3 if d >= 90 else 2 if d >= 80 else 0

def classify(s, d):
    return names[max(sys_rank(s), dia_rank(d))]

readings = [("Mon", "am", 128, 82), ("Mon", "pm", 121, 76), ("Tue", "am", 134, 79), ("Tue", "pm", 118, 74), ("Wed", "am", 142, 91), ("Wed", "pm", 126, 80), ("Thu", "am", 119, 78), ("Fri", "am", 131, 85), ("Fri", "pm", 117, 72)]
counts = {}
ms = md = mornings = 0
for day, when, s, d in readings:
    b = classify(s, d)
    counts[b] = counts.get(b, 0) + 1
    if when == "am":
        ms += s
        md += d
        mornings += 1
    print(f"{day} {when}: {s}/{d} {b}")
avg_s, avg_d = ms // mornings, md // mornings
print(f"morning average {avg_s}/{avg_d}: {classify(avg_s, avg_d)}")
for b in names:
    if counts.get(b, 0) > 0:
        print(f"{b}: {counts[b]}")

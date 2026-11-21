sl = ["08-10", "10-12", "12-14", "14-16", "16-18"]; load = [0] * 5; ta = []
for i, w in [("A1", 0), ("A2", 0), ("A3", 0), ("B1", 3), ("B2", 3), ("A4", 1), ("C1", 4), ("C2", 4), ("C3", 3), ("C4", 4)]:
    s = w
    while s < 5 and load[s] >= 2: s += 1
    if s == 5: ta.append(i); continue
    load[s] += 1
    print(f"{i} -> {sl[s]}" + ("" if s == w else f" (moved from {sl[w]})"))
print(f"load: {load}")
print("turned away: [" + ", ".join(f'"{x}"' for x in ta) + "]")

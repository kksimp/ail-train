ms = [72, 85, 72, 91, 60, 85, 85, 44, 100, 72, 58]
o = sorted(ms, reverse=True); rank = 0
for i, m in enumerate(o):
    if i == 0 or m != o[i - 1]: rank = i + 1
    print(f"{rank:>2}. {m}")
print(f"distinct marks: {len(set(ms))}")

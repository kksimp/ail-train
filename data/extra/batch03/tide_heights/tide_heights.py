h = [120, 150, 185, 210, 220, 205, 170, 130, 95, 70, 62, 75, 105, 145, 190, 225, 238, 226, 190, 150, 110, 80, 66, 72]
for i in range(1, len(h) - 1):
    if h[i] > h[i - 1] and h[i] >= h[i + 1]: print(f"high at {i:02d}:00, {h[i]} cm")
    elif h[i] < h[i - 1] and h[i] <= h[i + 1]: print(f"low  at {i:02d}:00, {h[i]} cm")
print(f"range {max(h) - min(h)} cm")
d = [i for i in range(len(h)) if h[i] >= 180]
print(f"deep enough: {len(d)} hours, first at {d[0]}:00")

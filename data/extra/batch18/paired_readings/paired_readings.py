trips = [412, 388, 520, 145]; fuel = [29.5, 27.0, 41.6, 12.4]
def per(km, l): return l * 100.0 / float(km)
for i in range(4):
    print(f"trip {i + 1}: {trips[i]} km, {per(trips[i], fuel[i]):.2f} l/100km")
tk = sum(trips); tl = 0.0
for l in fuel: tl = tl + l
print(f"overall {per(tk, tl):.2f} l/100km over {tk} km")
names = ["ann", "bo", "cy"]; scores = [17, 23, 9, 30]
labels = [f"{n}:{s}" for n, s in zip(names, scores)]
print(f"scores: {' '.join(labels)} ({len(labels)} paired)")
cost = [p * q for p, q in zip([250, 120, 75], [2, 5, 4])]
print(f"line costs {cost}, total {sum(cost)}")

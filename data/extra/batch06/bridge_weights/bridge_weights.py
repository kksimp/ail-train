T = [10, 8, 12, 4, 15, 7, 9, 3]; on = []; t = 0
for i, w in enumerate(T):
    while True:
        on = [x for x in on if x[1] > t]
        if sum(x[0] for x in on) + w <= 25: break
        t = min(x[1] for x in on)
    on.append((w, t + 3)); print(f"truck {i + 1} ({w} t) enters at {t}")
print(f"last off the bridge at {max(x[1] for x in on)}")

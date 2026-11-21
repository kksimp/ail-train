import heapq
def dwell(now, last_visit):
    waiting = (now - last_visit) // 2
    return 1 + waiting // 3
last = [0] * 12
events = [(0, 0, 0), (0, 1, 4), (6, 2, 8)]
heapq.heapify(events)
prev = -1
while events:
    t, b, s = heapq.heappop(events)
    if t > 500: break
    stay = dwell(t, last[s])
    last[s] = t
    if s == 0:
        gap = "first" if prev < 0 else f"{t - prev} min after the last bus"
        print(f"minute {t:>3}: bus {b + 1} at the depot stop, {gap}")
        prev = t
    heapq.heappush(events, (t + stay + 5, b, (s + 1) % 12))

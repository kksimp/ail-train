import heapq
def take(free, ready, minutes):
    at = heapq.heappop(free)
    start = max(at, ready)
    heapq.heappush(free, start + minutes)
    return start
names = ["Ada", "Bo", "Cy", "Di", "Ed", "Flo", "Gus", "Hal"]
arrive = [0, 5, 10, 12, 20, 25, 40, 41]
washers = [0, 0, 0]; dryers = [0, 0]
washed = []
for i in range(len(names)):
    start = take(washers, arrive[i], 30)
    washed.append([start + 30, i])
total_wait = 0
for w in sorted(washed):
    i = w[1]
    start = take(dryers, w[0], 45)
    done = start + 45
    wait = done - arrive[i] - 75
    total_wait += wait
    print(f"{names[i]:<4} arrives {arrive[i]:>2}, dry done at {done:>3}, waited {wait:>2} min")
print(f"total waiting {total_wait} min over {len(names)} loads")

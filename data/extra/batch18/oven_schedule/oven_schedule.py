import heapq
ov = [(0, 1), (0, 2)]
last = 0
for name, mins in [("sourdough", 45), ("baguettes", 25), ("croissants", 18), ("rye", 50), ("buns", 20), ("focaccia", 30)]:
    at, o = heapq.heappop(ov)
    done = at + mins
    print(f"{name:<10} oven {o} from {at:>3} to {done:>3}")
    heapq.heappush(ov, (done, o)); last = max(last, done)
print(f"all baked after {last} minutes")
print(f"oven {ov[0][1]} is free first, at {ov[0][0]}")

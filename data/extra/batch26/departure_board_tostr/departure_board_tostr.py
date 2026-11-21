flights = [("NA210", "LHR", "JFK", 520, 0), ("QS77", "CDG", "LHR", 495, 35), ("TR4410", "FRA", "LHR", 545, 0), ("ML903", "AMS", "LHR", 480, 10)]
def show(f):
    code, o, d, dep, delay = f
    t = dep + delay
    note = f" (+{delay} min)" if delay > 0 else ""
    return f"{code:<7}{o}-{d} {t // 60:02}:{t % 60:02}{note}"
for f in sorted(flights, key=lambda f: f[3] + f[4]):
    print(show(f))
late = [f for f in flights if f[4] > 0]
print(f"delayed: {len(late)}, total delay {sum(f[4] for f in late)} min")
print(f"leaving after 08:50: {sum(1 for f in flights if f[3] + f[4] > 530)}")

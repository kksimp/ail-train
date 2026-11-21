fl = [("KL1002", 189, 545, 1), ("BA0117", 412, 470, 0), ("IB6250", 156, 720, 2), ("LH0400", 233, 600, 1), ("VS0003", 398, 485, 0)]
def hm(m): return f"{m // 60}h{m % 60:02}"
f = min(fl, key=lambda f: f[1]); print(f"cheapest: {f[0]} at {f[1]}")
f = min(fl, key=lambda f: f[2]); print(f"quickest: {f[0]} in {hm(f[2])}")
f = max(fl, key=lambda f: f[2]); print(f"longest: {f[0]} in {hm(f[2])}")
f = min(fl, key=lambda f: (f[3], f[1])); print(f"fewest stops, then cheapest: {f[0]}")
print("direct: [" + ", ".join(f'"{f[0]}"' for f in fl if f[3] == 0) + "]")
print(f"average fare {sum(f[1] for f in fl) // len(fl)}")

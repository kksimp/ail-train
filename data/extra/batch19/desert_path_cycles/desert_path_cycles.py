def step(m, at, turn):
    return m[at][0] if turn == 'L' else m[at][1]

route = list("RRL")
lines = ["AAA = BBB, CCC", "BBB = DDD, AAA", "CCC = ZZZ, DDD", "DDD = CCC, ZZZ", "ZZZ = BBB, CCC", "MPA = MQB, MQB", "MQB = MRB, MRB", "MRB = MSB, MSB", "MSB = MTZ, MTZ", "MTZ = MQB, MQB"]
m = {}
for l in lines:
    k, v = l.split(" = "); m[k] = v.split(", ")
at = "AAA"; n = 0
while at != "ZZZ":
    at = step(m, at, route[n % len(route)]); n += 1
print(f"part 1: AAA reaches ZZZ in {n} steps")
walkers = [k for k in m if k.endswith("A")]
print(f"walkers start at {', '.join(walkers)}")
t = 0
while not all(w.endswith("Z") for w in walkers):
    turn = route[t % len(route)]
    walkers = [step(m, w, turn) for w in walkers]
    t += 1
print(f"part 2: all walkers stand on Z posts after {t} steps")

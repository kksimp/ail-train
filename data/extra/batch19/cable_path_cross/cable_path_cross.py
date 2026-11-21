def trace(path):
    seen = {}; x = y = steps = 0
    for m in path.split(","):
        for _ in range(int(m[1:])):
            d = m[0]
            if d == "R": x += 1
            elif d == "L": x -= 1
            elif d == "U": y += 1
            else: y -= 1
            steps += 1
            k = (x + 500) * 1000 + y + 500
            if k not in seen: seen[k] = steps
    return seen

a = trace("R6,U4,L9,D2,R5,U7"); b = trace("U3,R8,D6,L4,U9,R2")
nearest = quickest = 1000000; crossings = 0
for k, sa in a.items():
    if k in b:
        crossings += 1
        x = k // 1000 - 500; y = k % 1000 - 500
        print(f"  crossing at {x},{y} after {sa} + {b[k]} steps")
        nearest = min(nearest, abs(x) + abs(y)); quickest = min(quickest, sa + b[k])
print(f"{crossings} crossings")
print(f"part 1: nearest crossing is {nearest} from the socket")
print(f"part 2: fewest combined steps {quickest}")

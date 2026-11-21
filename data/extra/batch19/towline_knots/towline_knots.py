def sign(v):
    return 1 if v > 0 else (-1 if v < 0 else 0)

def trail(moves, knots):
    xs = [0] * knots; ys = [0] * knots
    seen = {500500}
    for line in moves:
        d, n = line.split(" ")
        for s in range(int(n)):
            if d == "R": xs[0] += 1
            elif d == "L": xs[0] -= 1
            elif d == "U": ys[0] += 1
            else: ys[0] -= 1
            for k in range(1, knots):
                dx = xs[k - 1] - xs[k]; dy = ys[k - 1] - ys[k]
                if abs(dx) > 1 or abs(dy) > 1:
                    xs[k] += sign(dx); ys[k] += sign(dy)
            seen.add((xs[knots - 1] + 500) * 1000 + ys[knots - 1] + 500)
    return len(seen)

moves = ["R 5", "U 3", "L 7", "D 2", "R 9", "U 6", "L 2", "D 8", "R 4", "U 1"]
total = sum(int(m.split(" ")[1]) for m in moves)
print(f"{len(moves)} pulls, {total} steps for the lead knot")
print(f"part 1, two knots: tail visits {trail(moves, 2)} cells")
print(f"part 2, six knots: tail visits {trail(moves, 6)} cells")
for k in [3, 4, 5]:
    print(f"  with {k} knots: {trail(moves, k)} cells")

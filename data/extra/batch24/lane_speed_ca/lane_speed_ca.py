size = 30
cars = [[p, 0] for p in [0, 1, 2, 3, 4, 5, 14, 22]]
def road(cars):
    cells = ["."] * size
    for p, v in cars: cells[p] = str(v)
    return "".join(cells)
def tick(cars, size):
    n = len(cars)
    speeds = []
    for k in range(n):
        gap = (cars[(k + 1) % n][0] - cars[k][0] - 1 + size) % size
        speeds.append(min(min(cars[k][1] + 1, 3), gap))
    for k in range(n):
        cars[k][1] = speeds[k]
        cars[k][0] = (cars[k][0] + speeds[k]) % size
moved = 0
for t in range(10):
    print(f"{t:>2} {road(cars)}")
    tick(cars, size)
    moved += sum(c[1] for c in cars)
print(f"mean speed over 10 ticks: {moved / 80.0:.3f} cells a tick")

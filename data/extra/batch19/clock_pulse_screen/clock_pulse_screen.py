def trace(prog):
    xs = []; x = 1
    for line in prog:
        parts = line.split(" ")
        xs.append(x)
        if parts[0] == "addx":
            xs.append(x); x += int(parts[1])
    xs.append(x)
    return xs

prog = ["addx 1", "noop", "addx 2", "addx -1", "noop", "addx 3", "addx 1", "noop", "addx 2", "addx -6", "noop", "addx 4", "addx 2", "addx 3", "noop", "addx -1"]
xs = trace(prog)
print(f"{len(prog)} instructions take {len(xs) - 1} cycles")
strength = 0
for cyc in [3, 9, 15, 21]:
    print(f"  cycle {cyc}: X = {xs[cyc - 1]}")
    strength += cyc * xs[cyc - 1]
print(f"part 1: signal strength {strength}")
print("part 2:")
for row in range(2):
    print("".join("#" if abs(xs[row * 12 + col] - col) <= 1 else "." for col in range(12)))

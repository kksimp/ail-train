lines = ["forward 4", "down 6", "forward 7", "up 2", "down 9", "forward 3", "up 5", "forward 6"]
cmds = [(l.split(" ")[0], int(l.split(" ")[1])) for l in lines]
print(f"{len(cmds)} commands")
x = depth = 0
for k, n in cmds:
    if k == "forward": x += n
    elif k == "down": depth += n
    else: depth -= n
print(f"part 1: ahead {x}, depth {depth}, product {x * depth}")
aim = x2 = d2 = 0
for k, n in cmds:
    if k == "forward":
        x2 += n; d2 += aim * n
    elif k == "down": aim += n
    else: aim -= n
print(f"part 2: ahead {x2}, depth {d2}, product {x2 * d2}")

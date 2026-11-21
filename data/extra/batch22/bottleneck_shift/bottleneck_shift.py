line = [["cut", 40, 1], ["weld", 12, 2], ["paint", 30, 1], ["pack", 50, 1]]

def cap(s):
    return s[1] * s[2]

for rnd in range(4):
    b = 0
    for i in range(1, len(line)):
        if cap(line[i]) < cap(line[b]):
            b = i
    output = cap(line[b])
    joined = ", ".join(f"{s[0]} {output * 100 // cap(s)}%" for s in line)
    print(f"round {rnd}: {output} an hour, bottleneck {line[b][0]} ({joined})")
    if rnd < 3:
        line[b][2] += 1

import sys

lines = [l for l in sys.stdin.read().splitlines() if l.strip()]
if not lines:
    print("no data")
else:
    cap, level = map(int, lines[0].split())
    over = 0
    short = 0
    for i, l in enumerate(lines[1:], 1):
        a, b = map(int, l.split())
        level += a
        if level > cap:
            over += level - cap
            level = cap
        level -= b
        if level < 0:
            short -= level
            level = 0
        print(f"step {i}: {level}")
    print(f"overflow {over} shortfall {short}")

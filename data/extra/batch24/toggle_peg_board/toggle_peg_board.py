def drop_ball(pegs):
    slot = 0
    for row in range(len(pegs)):
        right = pegs[row][slot]
        pegs[row][slot] = not right
        slot = slot * 2 + (1 if right else 0)
    return slot
pegs = [[False] * (1 << row) for row in range(4)]
bins = [0] * 16
order = []
for ball in range(32):
    b = drop_ball(pegs)
    bins[b] += 1
    if ball < 8: order.append(b)
print(f"first eight balls land in bins {order}")
print(f"bin counts after 32 balls {bins}")
print(f"pegs set to the right per row {[sum(1 for p in line if p) for line in pegs]}")

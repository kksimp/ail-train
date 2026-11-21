memo = {}
def best(tick, stamina):
    if tick == 12: return 0
    key = tick * 100 + stamina
    if key in memo: return memo[key]
    regen = lambda s: min(s + 2, 10)
    top = best(tick + 1, regen(stamina))
    if stamina >= 2: top = max(top, 3 + best(tick + 1, regen(stamina - 2)))
    if stamina >= 6: top = max(top, 11 + best(tick + 1, regen(stamina - 6)))
    memo[key] = top
    return top
total = best(0, 10)
plan = []; st = 10
for t in range(12):
    here = best(t, st)
    if st >= 6 and 11 + best(t + 1, min(st - 4, 10)) == here:
        plan.append('S'); st = min(st - 4, 10)
    elif st >= 2 and 3 + best(t + 1, min(st, 10)) == here:
        plan.append('j')
    else:
        plan.append('.'); st = min(st + 2, 10)
print(f"best plan {''.join(plan)}: {total} damage (S swing, j jab, . rest)")
greedy = 0; g = 10
for t in range(12):
    if g >= 6: greedy += 11; g -= 6
    elif g >= 2: greedy += 3; g -= 2
    g = min(g + 2, 10)
print(f"swing when you can, else jab: {greedy} damage")
print(f"{len(memo)} states searched")

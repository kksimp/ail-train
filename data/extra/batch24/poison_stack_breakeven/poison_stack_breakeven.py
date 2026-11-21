def blade_b(ticks):
    total = 0; stacks = []
    for t in range(ticks):
        total += 8
        stacks.append(4)
        total += 4 * len(stacks)
        stacks = [s - 1 for s in stacks if s - 1 > 0]
    return total
even = -1
for ticks in range(1, 9):
    a = 20 * ticks; b = blade_b(ticks)
    lead = "B ahead" if b > a else "level" if b == a else "A ahead"
    print(f"{ticks} ticks: A {a:>3}, B {b:>3}  {lead}")
    if even < 0 and b >= a: even = ticks
print(f"B catches up from a fight of {even} ticks; its steady rate is {8 + 4 * 4} a tick")

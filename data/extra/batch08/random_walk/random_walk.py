def nx(x): return (1103515245 * x + 12345) % 2147483648
seed = 2026; pos = 0; far = 0; ret = 0
for step in range(1, 201):
    seed = nx(seed); pos += 1 if ((seed >> 16) & 1) == 1 else -1
    far = max(far, abs(pos)); ret += pos == 0
    if step % 40 == 0: print(f"step {step:>3}: position {pos:>3}")
print(f"furthest {far} steps away, back at the start {ret} times")
x = y = 0
for step in range(400):
    seed = nx(seed); d = (seed >> 16) % 4
    if d == 0: x += 1
    elif d == 1: x -= 1
    elif d == 2: y += 1
    else: y -= 1
print(f"400 steps on a grid end at ({x}, {y}), {(x * x + y * y) ** 0.5:.2f} from the start")

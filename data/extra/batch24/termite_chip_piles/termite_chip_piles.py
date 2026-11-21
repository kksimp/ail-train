state = 2468
def below(n):
    global state
    state = (state * 1103515245 + 12345) % 2147483648
    return (state // 65536) % n
def show(cells): return "".join("." if n == 0 else str(min(n, 9)) for n in cells)
cells = [1 if below(3) == 0 else 0 for i in range(30)]
pos = [0, 10, 20]; carrying = [False, False, False]
print(f"start      {show(cells)}")
for step in range(1, 3001):
    for t in range(3):
        pos[t] = (pos[t] + 29 + 2 * below(2)) % 30
        if not carrying[t] and cells[pos[t]] > 0:
            cells[pos[t]] -= 1; carrying[t] = True
        elif carrying[t] and cells[pos[t]] > 0:
            cells[pos[t]] += 1; carrying[t] = False
    if step % 600 == 0:
        piles = sum(1 for n in cells if n > 0)
        print(f"step {step:>4}  {show(cells)}  {piles} piles")
held = sum(1 for c in carrying if c)
print(f"chips on the ground {sum(cells)}, in jaws {held}")

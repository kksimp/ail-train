size = 6
body = [(2, 2), (1, 2), (0, 2)]; food = [(4, 2), (4, 4), (0, 4)]
def st(h, d):
    x, y = h
    return {"U": (x, (y - 1) % size), "D": (x, (y + 1) % size), "L": ((x - 1) % size, y)}.get(d, ((x + 1) % size, y))
alive = True
for i, d in enumerate("RRDDLLLLUUUR"):
    h = st(body[0], d); ate = h in food
    if not ate: body.pop()
    if h in body: print(f"move {i + 1}: crashed at {h}"); alive = False; break
    body.insert(0, h)
    if ate: food.remove(h); print(f"move {i + 1}: ate at {h}, length {len(body)}")
if alive: print(f"survived, head {body[0]}, length {len(body)}")

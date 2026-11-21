state = 555
def below(n):
    global state
    state = (state * 1103515245 + 12345) % 2147483648
    return (state // 65536) % n
def cut(p, out):
    x, y, w, h = p
    if w <= 10 and h <= 10:
        out.append(p); return
    share = 40 + below(21)
    if w >= h:
        left = w * share // 100
        cut((x, y, left, h), out)
        cut((x + left, y, w - left, h), out)
    else:
        top = h * share // 100
        cut((x, y, w, top), out)
        cut((x, y + top, w, h - top), out)
plots = []
cut((0, 0, 32, 20), plots)
for x, y, w, h in sorted(plots, key=lambda q: (q[1], q[0])):
    print(f"plot at ({x:>2},{y:>2}) {w:>2} x {h:>2} = {w * h:>3}")
area = sum(w * h for x, y, w, h in plots)
print(f"{len(plots)} plots covering {area} of 640 square units")

b = [(2, 2), (2, 1), (2, 0)]; fd = [(2, 4), (4, 4), (4, 1)]; st = 0; s = "finished"
for m in "RRDDLLLUUR":
    r, c = b[0]; r, c = {"R": (r, c + 1), "L": (r, c - 1), "U": (r - 1, c), "D": (r + 1, c)}[m]; cl = (r, c)
    if not (0 <= r <= 5 and 0 <= c <= 5): s = f"hit wall at step {st + 1}"; break
    if cl in b: s = f"hit itself at step {st + 1}"; break
    b.insert(0, cl)
    if cl in fd: fd.remove(cl); print(f"ate at {r},{c}, length {len(b)}")
    else: b.pop()
    st += 1
print(f"{s} after {st} steps, head at {b[0][0]},{b[0][1]}")

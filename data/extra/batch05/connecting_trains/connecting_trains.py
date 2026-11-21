T = [("A", "B", 480, 530), ("A", "C", 490, 600), ("B", "C", 540, 580), ("B", "D", 545, 640), ("C", "D", 590, 620), ("C", "E", 610, 700), ("D", "E", 630, 690), ("A", "E", 500, 720)]; B = {"A": 470}
for f, t, d, a in sorted(T, key=lambda x: (x[2], x[0])):
    if f in B and B[f] <= d and a < B.get(t, 100000): B[t] = a
for s in "ABCDE": print(f"{s}: {B[s] // 60:02}:{B[s] % 60:02}" if s in B else f"{s}: unreachable")

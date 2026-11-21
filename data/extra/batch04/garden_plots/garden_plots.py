P = [("A1", 450, 300), ("A2", 500, 520), ("B1", 380, 410), ("B2", 610, 350), ("C1", 250, 900)]
m2 = lambda c: f"{c // 100 // 100}.{c // 100 % 100:02d}"
for n, w, l in P: print(f"{n}: {w} x {l} cm = {m2(w * l)} m2")
print(f"total {m2(sum(w * l for _, w, l in P))} m2")
print("need a water butt: " + " ".join(n for n, w, l in P if w * l > 200000))

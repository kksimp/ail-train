P = [("Ros", "Mon", 2350), ("Sam", "Tue", 4100), ("Ros", "Tue", 1875), ("Tia", "Fri", 12990), ("Sam", "Sat", 6720), ("Ros", "Thu", 5600), ("Tia", "Tue", 3300)]; pt = {}
for w, d, p in P: pt[w] = pt.get(w, 0) + (p // 100 * 2 if d == "Tue" else p // 100)
for w in sorted(pt): v = pt[w] // 100; print(f"{w}: {pt[w]} points, {v} voucher(s) worth {v * 5}, {pt[w] % 100} carried")

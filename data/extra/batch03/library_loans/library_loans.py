loans = [("Tides", 1, 10), ("Kites", 3, 22), ("Moths", 5, None), ("Ferns", 20, None), ("Bells", 2, 16)]
today = 30
def out(l): return (l[2] if l[2] is not None else today) - l[1]
def fine(l):
    late = out(l) - 14
    return late * 25 if late > 0 else 0
for l in loans:
    st = "out" if l[2] is None else "back"
    print(f"{l[0]:<6} {st:<4} {out(l):>2} days, fine {fine(l)}c")
print(f"fines {sum(fine(l) for l in loans)}c, still out {sum(1 for l in loans if l[2] is None)}")

def o(n):
    s = "th" if 11 <= n % 100 <= 13 else {1: "st", 2: "nd", 3: "rd"}.get(n % 10, "th")
    return f"{n}{s}"
print(" ".join(o(n) for n in [1, 2, 3, 4, 11, 12, 13, 21, 22, 23, 101, 111, 112, 1003]))
for i, (n, t) in enumerate(sorted([("Rui", 1312), ("Sam", 1288), ("Tia", 1401), ("Uli", 1295), ("Vee", 1350)], key=lambda r: r[1])):
    print(f"{o(i + 1):>4} {n} {t // 60}:{t % 60:02d}")

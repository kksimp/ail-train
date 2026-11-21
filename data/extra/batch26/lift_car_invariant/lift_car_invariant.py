floor, top, load, cap = 0, 10, 0, 320
trav = 0
for op, n in [("in", 80), ("in", 75), ("in", 90), ("in", 100), ("go", 7), ("out", 75), ("in", 100), ("go", 12), ("out", 300), ("go", 0)]:
    if op == "in":
        ok = load + n <= cap
        if ok: load += n
        print(f"{n} kg {'boards' if ok else 'refused'}, load {load}/{cap}")
    elif op == "out":
        load = max(load - n, 0)
        print(f"{n} kg leaves, load {load}")
    else:
        t = min(n, top); trav += abs(t - floor); floor = t
        print(f"to floor {floor} (asked {n})")
print(f"travelled {trav} floors")

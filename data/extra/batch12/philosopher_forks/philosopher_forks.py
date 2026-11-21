def simulate(ordered, ticks):
    forks = [-1] * 5
    st = [("H", 0)] * 5
    meals = [0] * 5
    for t in range(ticks):
        changed = False
        for i in range(5):
            a = min(i, (i + 1) % 5) if ordered else i
            b = max(i, (i + 1) % 5) if ordered else (i + 1) % 5
            kind, n = st[i]
            if kind == "T":
                st[i] = ("H", 0) if n <= 1 else ("T", n - 1)
                changed = True
            elif kind == "E":
                changed = True
                if n <= 1:
                    forks[a] = -1
                    forks[b] = -1
                    meals[i] += 1
                    st[i] = ("T", 2)
                else:
                    st[i] = ("E", n - 1)
            else:
                if forks[a] == -1:
                    forks[a] = i
                    changed = True
                elif forks[a] == i and forks[b] == -1:
                    forks[b] = i
                    st[i] = ("E", 2)
                    changed = True
        if not changed:
            return f"deadlock at tick {t}: every diner holds one fork"
    return f"after {ticks} ticks meals are {meals}"

print(f"left first:   {simulate(False, 30)}")
print(f"lowest first: {simulate(True, 30)}")
print(f"lowest first, short run: {simulate(True, 6)}")

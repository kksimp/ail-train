tables = [2, 2, 4, 4, 6]
free_at = [0] * 5
parties = [("Ito", 0, 2, 50), ("Kahn", 5, 5, 70), ("Lee", 8, 4, 60), ("Moss", 10, 6, 80), ("Nair", 12, 3, 45), ("Olsen", 15, 2, 40), ("Park", 20, 4, 55), ("Quist", 25, 2, 30)]
def smallest_free(tables, free_at, size, now):
    pick = -1
    for i in range(len(tables)):
        if free_at[i] <= now and tables[i] >= size and (pick < 0 or tables[i] < tables[pick]): pick = i
    return pick
waiting = []; seated = 0; now = 0; total_wait = 0
while seated < len(parties):
    for i, p in enumerate(parties):
        if p[1] == now: waiting.append(i)
    still = []
    for i in waiting:
        name, arrive, size, stay = parties[i]
        t = smallest_free(tables, free_at, size, now)
        if t < 0: still.append(i)
        else:
            free_at[t] = now + stay
            seated += 1
            total_wait += now - arrive
            print(f"{now:>3}: {name:<6} ({size}) at the {tables[t]}-seat table, waited {now - arrive}")
    waiting = still
    now += 1
print(f"mean wait {total_wait / len(parties):.3f} minutes")

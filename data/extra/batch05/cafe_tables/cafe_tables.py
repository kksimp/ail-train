T = [2, 2, 4, 4, 6]; F = [0] * 5
for a, s, st in [(0, 2, 30), (5, 4, 45), (10, 5, 50), (12, 2, 25), (15, 3, 40), (20, 6, 60), (25, 2, 20), (40, 4, 30)]:
    p = -1; sb = 10 ** 6
    for i in range(5):
        if T[i] >= s:
            r = max(F[i], a)
            if r < sb or (r == sb and T[i] < T[p]): sb = r; p = i
    F[p] = sb + st; print(f"party of {s} at {a}: table {p + 1} (seats {T[p]}) at {sb}, waited {sb - a}")

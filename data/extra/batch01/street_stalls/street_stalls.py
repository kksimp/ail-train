def best_choice(t):
    n = len(t)
    if n == 0: return 0, []
    b = [0] * n; b[0] = t[0]
    for i in range(1, n):
        b[i] = max(b[i - 1], t[i] + (b[i - 2] if i >= 2 else 0))
    ch, i = [], n - 1
    while i >= 0:
        prev = b[i - 1] if i >= 1 else 0
        if b[i] != prev:
            ch.append(i); i -= 2
        else:
            i -= 1
    return b[n - 1], ch[::-1]
for st in [[6, 7, 1, 30, 8, 2, 4], [5, 5, 10, 100, 10, 5], [3], [], [4, 1, 1, 4]]:
    tot, p = best_choice(st)
    print(f"{','.join(map(str, st))}: {tot} from stalls {' '.join(str(x + 1) for x in p)}")

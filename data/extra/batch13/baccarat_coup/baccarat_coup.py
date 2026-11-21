def banker_draws(total, third):
    if total in (0, 1, 2):
        return True
    if total == 3:
        return third != 8
    if total == 4:
        return 2 <= third <= 7
    if total == 5:
        return 4 <= third <= 7
    if total == 6:
        return third in (6, 7)
    return False

def play(c):
    p = (c[0] + c[1]) % 10
    b = (c[2] + c[3]) % 10
    if p >= 8 or b >= 8:
        return f"natural, player {p} banker {b}"
    nxt = 4
    drew = "player stands"
    if p <= 5:
        third = c[nxt]
        nxt += 1
        p = (p + third) % 10
        drew = f"player draws {third}"
        if banker_draws(b, third):
            b = (b + c[nxt]) % 10
            drew = f"{drew}, banker draws {c[nxt]}"
    elif b <= 5:
        b = (b + c[nxt]) % 10
        drew = f"{drew}, banker draws {c[nxt]}"
    result = "player wins" if p > b else ("banker wins" if b > p else "tie")
    return f"{drew}: player {p} banker {b}, {result}"

coups = [[3, 4, 5, 3, 2, 1], [9, 0, 2, 5, 7, 7], [2, 1, 3, 0, 8, 6], [6, 0, 4, 1, 5, 3], [0, 4, 6, 0, 6, 2], [7, 0, 3, 2, 9, 4], [1, 2, 4, 2, 3, 5]]
for i, c in enumerate(coups):
    print(f"coup {i + 1}: {play(c)}")

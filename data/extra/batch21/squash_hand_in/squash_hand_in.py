def play(rallies):
    a = b = 0
    server = "A"
    outs = 0
    for w in rallies:
        if w == server:
            if server == "A":
                a += 1
            else:
                b += 1
        else:
            server = w
            outs += 1
        if a == 9 or b == 9:
            break
    return [a, b, outs]

rallies = "AAABBABAAABBBBAABABAAAAABBBAAAB"
a = b = 0
server = "A"
marks = []
streak = best = 0
for w in rallies:
    if w == server:
        streak += 1
        best = max(best, streak)
        if server == "A":
            a += 1
        else:
            b += 1
    else:
        server = w
        streak = 0
        marks.append(f"{a}-{b}")
    if a == 9 or b == 9:
        break
print(f"hand-outs at: {', '.join(marks)}")
r = play(rallies)
print(f"game {r[0]}-{r[1]} after {r[2]} hand-outs")
print(f"longest run of points on one serve: {best}")
print(f"winner: player {'A' if r[0] > r[1] else 'B'}")

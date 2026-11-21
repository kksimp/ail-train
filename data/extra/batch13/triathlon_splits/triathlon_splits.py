field = [("Brownlee", [1080, 45, 3420, 28, 1890]), ("Duffy", [1110, 52, 3380, 31, 1925]), ("Gomez", [1135, 40, 3465, 25, 1840]), ("Jorgensen", [1100, 61, 3400, 35, 1870])]

def hms(t):
    return f"{t // 3600}:{t // 60 % 60:02}:{t % 60:02}"

leg_names = ["swim", "T1", "bike", "T2", "run"]
for k in [0, 2, 4]:
    best = sorted(field, key=lambda a: a[1][k])
    names = " > ".join(a[0] for a in best)
    print(f"{leg_names[k]:<4} {names}")
ranked = sorted(field, key=lambda a: sum(a[1]))
winner = sum(ranked[0][1])
for i, a in enumerate(ranked):
    transitions = a[1][1] + a[1][3]
    behind = sum(a[1]) - winner
    print(f"{i + 1}. {a[0]:<10} {hms(sum(a[1]))}  +{behind:>3}s  transitions {transitions}s")

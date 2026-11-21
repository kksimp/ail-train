D = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
def wd(s):
    d = s
    while True:
        if d % 7 < 5: yield d
        d += 1
import itertools
team = ["Ana", "Bram", "Chidi"]
for i, d in enumerate(itertools.islice(wd(3), 7)): print(f"{D[d % 7]} {d}: {team[i % 3]} runs stand-up")
fr = list(itertools.islice((d for d in wd(0) if d % 7 == 4), 3))
print(f"next demos: {', '.join(f'{D[d % 7]} {d}' for d in fr)}")
print(f"tenth working day is day {list(itertools.islice(wd(0), 9, 10))[0]}")

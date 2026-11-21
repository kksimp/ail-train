spells = [("Akram", 60, 2, 38, 3), ("Bond", 57, 0, 61, 1), ("Cairns", 42, 1, 29, 0), ("Dravid", 27, 0, 22, 2), ("Elgar", 54, 1, 47, 4)]

def overs(balls):
    return f"{balls // 6}.{balls % 6}"

print("bowler     O     M   R  W   econ")
for b, balls, m, runs, w in spells:
    econ = float(runs) * 6.0 / float(balls)
    print(f"{b:<7} {overs(balls):>5} {m:>3} {runs:>3} {w:>2} {econ:>6.2f}")
for b, balls, m, runs, w in sorted([x for x in spells if x[4] > 0], key=lambda x: x[3] * 1000 // x[4]):
    avg = float(runs) / float(w)
    sr = float(balls) / float(w)
    print(f"{b}: average {avg:.2f}, a wicket every {sr:.1f} balls")
total = sum(x[1] for x in spells)
print(f"innings: {overs(total)} overs")

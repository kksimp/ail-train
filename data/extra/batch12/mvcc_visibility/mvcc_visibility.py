versions = [("pen", 120, 1, 4), ("pen", 135, 4, 0), ("cap", 900, 2, 0), ("mug", 450, 3, 6), ("mug", 480, 6, 0), ("bag", 2500, 5, 0)]
aborted = [5]

def done(snap, tx):
    upto, active = snap
    return tx > 0 and tx < upto and tx not in active and tx not in aborted

def sees(snap, v):
    return done(snap, v[2]) and not done(snap, v[3])

snaps = [("snapshot at 3, T2 running", (3, [2])), ("snapshot at 5, T4 running", (5, [4])), ("snapshot at 7, none running", (7, [])), ("snapshot at 7, T6 running", (7, [6]))]
for label, snap in snaps:
    seen = [f"{v[0]}={v[1]}" for v in versions if sees(snap, v)]
    print(f"{label}: {' '.join(seen)}")

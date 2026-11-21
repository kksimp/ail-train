batters = [("Ortega", 540, 110, 35, 3, 28, 70, 6, 5), ("Kim", 600, 150, 30, 8, 6, 45, 2, 4), ("Walsh", 410, 60, 22, 0, 31, 88, 9, 3)]
def hits(b):
    return b[2] + b[3] + b[4] + b[5]
def bases(b):
    return b[2] + 2 * b[3] + 3 * b[4] + 4 * b[5]
def rate(n, d):
    return float(n) / float(d)
for b in batters:
    avg = rate(hits(b), b[1])
    obp = rate(hits(b) + b[6] + b[7], b[1] + b[6] + b[7] + b[8])
    slg = rate(bases(b), b[1])
    print(f"{b[0]:<7} {hits(b):>3} H: AVG {avg:.3f}, OBP {obp:.3f}, SLG {slg:.3f}, OPS {obp + slg:.3f}")
power = max(batters, key=bases)
print(f"most total bases: {power[0]} ({bases(power)})")

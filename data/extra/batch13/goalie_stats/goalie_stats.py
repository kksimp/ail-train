goalies = [("Hasek", 1840, 151, 223560), ("Ivers", 960, 92, 121905), ("Juneau", 412, 30, 51210), ("Kask", 1322, 120, 168035)]

def clock(seconds):
    return f"{seconds // 60}:{seconds % 60:02}"

print("goalie    TOI         SA   GA   SV%   GAA")
for name, shots, goals, seconds in goalies:
    p = float(shots - goals) / float(shots)
    sv = f"{p:.3f}"[1:]
    gaa = float(goals * 3600) / float(seconds)
    print(f"{name:<7} {clock(seconds):>9} {shots:>6} {goals:>4} {sv} {gaa:>5.2f}")
best = sorted([g for g in goalies if g[3] >= 60000], key=lambda g: g[2] * 100000000 // g[1])
print(f"best save rate with 1000 minutes: {best[0][0]}")

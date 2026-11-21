import math

def rel_rate(m, ref_m):
    return math.sqrt(ref_m / m)

for name, m in [("hydrogen", 2.016), ("helium", 4.003), ("methane", 16.04), ("oxygen", 32.0), ("carbon dioxide", 44.01), ("sulfur hexafluoride", 146.06)]:
    r = rel_rate(m, 32.0)
    secs = 60.0 / r
    print(f"{name:<20} {m:>7.2f} g/mol: {r:.3f}x oxygen's rate, 1 L leaks in {secs:>6.1f} s")
alpha = rel_rate(349.03, 352.04)
print(f"U-235 F6 against U-238 F6: separation factor {alpha:.5f} per stage")
start = 0.0072 / (1.0 - 0.0072)
target = 0.03 / (1.0 - 0.03)
stages = int(math.ceil(math.log(target / start) / math.log(alpha)))
print(f"0.72% to 3% U-235 takes {stages} ideal stages")

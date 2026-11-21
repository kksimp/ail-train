def effort(load_n, falls):
    keep = 0.96
    return load_n / (float(falls) * keep ** float(falls))
load_n = 1900.0
lift = 3.0
print(f"load {load_n} N, lifted {lift} m")
for falls in range(1, 7):
    ideal = load_n / float(falls)
    real = effort(load_n, falls)
    rope = lift * float(falls)
    eff = ideal / real * 100.0
    print(f"{falls} falls: ideal {ideal:>6.1f} N, real {real:>6.1f} N, efficiency {eff:>4.1f}%, pull {rope:>4.1f} m of rope")
best = 1
for falls in range(2, 41):
    if effort(load_n, falls) < effort(load_n, best):
        best = falls
print(f"least effort with {best} falls")

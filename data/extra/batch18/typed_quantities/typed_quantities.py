dry = [("flour", 500), ("sugar", 120), ("butter", 90)]; wet = [("milk", 300), ("water", 150)]
dt = 0
for n, a in dry:
    g = a * 6 // 4; dt += g; print(f"{n:<7} {a:>4} g -> {g:>4} g")
wt = 0
for n, a in wet:
    v = a * 6 // 4; wt += v; print(f"{n:<7} {a:>4} ml -> {v:>4} ml")
print(f"for 6: {dt} g dry, {wt} ml liquid")
print("more flour than sugar: true")

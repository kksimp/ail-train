stages = [(3, 8), (2, 5)]

def build(target):
    rows = []
    want = target
    for s in reversed(stages):
        parts = 1 + 2 * s[0]
        seed = (want + parts - 1) // parts
        rows.insert(0, [seed, seed * s[0], seed * s[0]])
        want = seed
    return rows

def clock(t):
    day = "Fri" if t < 1440 else "Sat"
    m = t % 1440
    return f"{day} {m // 60:02d}:{m % 60:02d}"

bake = 1440 + 9 * 60
for loaves in range(1, 4):
    target = 180 * loaves
    rows = build(target)
    t = bake - sum(s[1] * 60 for s in stages)
    print(f"{loaves} loaf, {target} g levain, from {rows[0][0]} g of jar starter:")
    for i, row in enumerate(rows):
        print(f"  {clock(t)} feed {row[0]} g seed + {row[1]} g flour + {row[2]} g water")
        t += stages[i][1] * 60
print(f"bake at {clock(bake)}")

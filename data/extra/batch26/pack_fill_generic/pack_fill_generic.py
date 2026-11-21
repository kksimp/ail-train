def fill(items, cap, label):
    out = []; used = 0
    for it in items:
        if used + it[1] > cap:
            print(f"  no room for {label(it)}")
            continue
        used += it[1]; out.append(it)
    return out
gear = [("tent", 1800), ("stove", 450), ("sleeping bag", 1100), ("chair", 900), ("lantern", 300)]
print("backpack, limit 3500 g:")
pack = fill(gear, 3500, lambda g: g[0])
print(f"packed {', '.join(g[0] for g in pack)}: {sum(g[1] for g in pack)} g")
snacks = [("apple", 180, 95), ("crackers", 120, 480), ("cheese", 150, 600), ("chocolate", 100, 530)]
print("lunchbox, limit 400 g:")
lunch = fill(snacks, 400, lambda s: f"{s[0]} ({s[2]} kcal)")
print(f"packed {len(lunch)} snacks: {sum(s[2] for s in lunch)} kcal")

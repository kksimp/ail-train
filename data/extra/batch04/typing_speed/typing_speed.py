T = "pack my box with five dozen liquor jugs and then rest".split(" ")
for w, t, s in [("Ann", "pack my box with five dozen liquor jugs and then rest", 21), ("Ben", "pack my bix with fiev dozen liquor jugs and than rest", 15), ("Cy", "pack my box with five dozen", 9)]:
    ws = t.split(" "); r = sum(1 for i, x in enumerate(ws) if i < len(T) and x == T[i])
    print(f"{w}: {r}/{len(ws)} right, {len(ws) * 60 / s:.1f} wpm, {r * 100 / len(ws):.0f}% accurate")

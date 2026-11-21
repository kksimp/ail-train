target, boost, away, on = 160, 0, 0, False
cmds = [("S", 205), ("B", 30), ("B", 15), ("S", 190), ("A", 3), ("O", 0)]
for i, (k, v) in enumerate(cmds):
    if k == "S":
        target = v; on = True; msg = f"target {v // 10}.{v % 10} C"
    elif k == "B":
        boost += v; msg = f"boost for {boost} min"
    elif k == "A":
        away = v; target = 120; msg = f"away {v} days, holding 12.0 C"
    else:
        on = False; boost = 0; msg = "heating off"
    print(f"{i + 1}. {msg}")
print(f"Heater(target: {target}, boost: {boost}, away: {away}, on: {'true' if on else 'false'})")
print(f"boost minutes asked for: {sum(v for k, v in cmds if k == 'B')}")

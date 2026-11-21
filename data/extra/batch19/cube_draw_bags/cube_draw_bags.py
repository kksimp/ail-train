def needs(line):
    n = {"amber": 0, "jade": 0, "onyx": 0}
    for hand in line.split(": ")[1].split("; "):
        for part in hand.split(", "):
            c, col = part.split(" ")
            n[col] = max(n[col], int(c))
    return n

games = ["Game 1: 4 amber, 2 jade; 7 onyx, 1 amber; 3 jade", "Game 2: 12 amber, 1 onyx; 5 jade", "Game 3: 2 jade, 2 onyx, 2 amber; 9 onyx; 6 amber, 11 jade", "Game 4: 8 onyx; 1 jade, 13 onyx", "Game 5: 3 amber, 4 jade, 5 onyx; 10 amber"]
p1 = p2 = 0
for g in games:
    gid = int(g.split(":")[0].split(" ")[1])
    n = needs(g)
    ok = n["amber"] <= 10 and n["jade"] <= 11 and n["onyx"] <= 12
    power = n["amber"] * n["jade"] * n["onyx"]
    verdict = "possible" if ok else "impossible"
    print(f"game {gid}: needs {n['amber']}/{n['jade']}/{n['onyx']}, power {power}, {verdict}")
    if ok: p1 += gid
    p2 += power
print(f"part 1: {p1}")
print(f"part 2: {p2}")

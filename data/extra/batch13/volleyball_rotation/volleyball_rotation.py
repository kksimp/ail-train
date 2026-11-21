teams = [{"name": "Hawks", "players": ["Ida", "Jo", "Kit", "Lu", "Max", "Ned"], "points": 0}, {"name": "Owls", "players": ["Pia", "Quin", "Rae", "Sol", "Tam", "Uma"], "points": 0}]
rallies = "HHOOHOOOHHHOHO"
serving = 0
servers = []
for r in rallies:
    winner = 0 if r == 'H' else 1
    servers.append(teams[serving]["players"][0])
    teams[winner]["points"] += 1
    if winner != serving:
        pl = teams[winner]["players"]
        pl.append(pl.pop(0))
        serving = winner
        print(f"side out: {teams[winner]['name']} rotate, {pl[0]} to serve")
print(f"servers in order: {' '.join(servers)}")
for t in teams:
    court = ", ".join(t["players"])
    print(f"{t['name']} {t['points']}: zones 1-6 {court}")

def rounds(teams):
    ts = list(teams)
    if len(ts) % 2: ts.append("bye")
    n = len(ts); out = []
    for _ in range(n - 1):
        out.append([(ts[i], ts[n - 1 - i]) for i in range(n // 2)])
        ts.insert(1, ts.pop())
    return out
def sh(g):
    if g[1] == "bye": return f"{g[0]} rests"
    if g[0] == "bye": return f"{g[1]} rests"
    return f"{g[0]}-{g[1]}"
for teams in [["Ajax", "Bari", "Celta", "Derby"], ["Elche", "Fulham", "Genk"]]:
    print(f"{len(teams)} teams:")
    for r, gs in enumerate(rounds(teams)):
        print(f"  round {r + 1}: " + ", ".join(sh(g) for g in gs))
al = [g for r in rounds(list("abcdef")) for g in r]
print(f"6 teams: {len(al)} games, {len({''.join(sorted(g)) for g in al})} distinct pairs")

def rounds_to_kill(hp, per_round):
    if per_round <= 0: return 1000
    return (hp + per_round - 1) // per_round
knight_needs = rounds_to_kill(80, 14)
best = -1; best_gap = 1000
for a in range(6, 17):
    rogue_needs = rounds_to_kill(120, 2 * (a - 3))
    verdict = "rogue" if rogue_needs < knight_needs else "knight" if rogue_needs > knight_needs else "draw"
    print(f"A {a:>2}: rogue needs {rogue_needs:>2} rounds, knight {knight_needs} -> {verdict}")
    gap = abs(rogue_needs - knight_needs)
    if gap < best_gap:
        best_gap = gap; best = a
print(f"closest fight at A = {best}")

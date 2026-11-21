cands = ["Ivy", "Jun", "Kai", "Lev"]
ballots = [(14, [5, 4, 0, 1]), (10, [4, 3, 1, 0]), (11, [0, 5, 5, 2]), (9, [0, 5, 3, 0]), (7, [5, 0, 0, 5]), (3, [3, 3, 3, 3])]
totals = [0, 0, 0, 0]
voters = 0
for count, scores in ballots:
    voters += count
    for i in range(4):
        totals[i] += count * scores[i]
order = sorted(range(4), key=lambda i: -totals[i])
for i in order:
    avg = totals[i] / voters
    print(f"{cands[i]:<4} {totals[i]:>4} points, mean {avg:.2f}")
a = order[0]
b = order[1]
for_a = for_b = level = 0
for count, scores in ballots:
    if scores[a] > scores[b]:
        for_a += count
    elif scores[b] > scores[a]:
        for_b += count
    else:
        level += count
winner = cands[a] if for_a >= for_b else cands[b]
print(f"runoff {cands[a]} {for_a} - {for_b} {cands[b]} ({level} no preference)")
upset = ", beating the score leader" if winner != cands[a] else ""
print(f"winner {winner}{upset}")

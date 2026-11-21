def settle(row):
    score = 0
    while len(row) >= 3:
        hit = -1
        for i in range(len(row) - 2):
            if row[i] == row[i+1] and row[i+1] == row[i+2]: hit = i; break
        if hit < 0: break
        level = row[hit]
        del row[hit]; del row[hit]
        row[hit] = level + 1
        score += 3 * level
    return score
gems = [1, 2, 1, 1, 3, 2, 2, 1, 3, 1, 2, 2, 3, 1, 1, 2, 3, 3, 1, 2]
row = []; total = 0
for i, g in enumerate(gems):
    best_score = -1; best_row = row; best_pos = 0
    for pos in range(len(row) + 1):
        trial = row[:pos] + [g] + row[pos:]
        got = settle(trial)
        if got > best_score:
            best_score = got; best_row = trial; best_pos = pos
    row = best_row
    total += best_score
    if best_score > 0:
        shown = "".join(map(str, row))
        print(f"gem {i + 1:>2} (level {g}) into gap {best_pos}: {shown:<8} +{best_score}")
print(f"final row {''.join(map(str, row))}, {len(row)} gems, score {total}")

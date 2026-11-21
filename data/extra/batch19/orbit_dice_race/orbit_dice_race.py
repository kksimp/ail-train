def wins(p1, s1, p2, s2, memo):
    if s2 >= 15: return [0, 1]
    key = (p1, s1, p2, s2)
    if key in memo: return memo[key]
    total = [0, 0]
    for a in range(1, 4):
        for b in range(1, 4):
            for c in range(1, 4):
                pos = (p1 + a + b + c - 1) % 8 + 1
                sub = wins(p2, s2, pos, s1 + pos, memo)
                total[0] += sub[1]; total[1] += sub[0]
    memo[key] = total
    return total

starts = [3, 7]
pos = list(starts); score = [0, 0]; die = 0; rolls = 0; turn = 0
while score[0] < 300 and score[1] < 300:
    moved = 0
    for _ in range(3):
        die = die % 50 + 1; moved += die; rolls += 1
    pos[turn] = (pos[turn] + moved - 1) % 8 + 1
    score[turn] += pos[turn]
    turn = 1 - turn
print(f"counting die: scores {score} after {rolls} rolls")
print(f"part 1: loser x rolls = {min(score) * rolls}")
w = wins(starts[0], 0, starts[1], 0, {})
print(f"split die to 15: pawn 1 wins in {w[0]} games, pawn 2 in {w[1]}")
print(f"part 2: {max(w)}")

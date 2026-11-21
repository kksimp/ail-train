per_row = [2, 0, 4, 0, 2, 0, 6, 0, 2, 0, 4, 0]
goal = 8 * len(per_row)

def locate(total, rows):
    return [(total - 1) // rows + 1, (total - 1) % rows + 1]

def yarn_overs(done):
    return done // len(per_row) * sum(per_row) + sum(per_row[:done % len(per_row)])

for done in [1, 12, 13, 50, 77, 96]:
    at = locate(done, len(per_row))
    print(f"row {done:>2}: repeat {at[0]}, chart row {at[1]:>2}, {yarn_overs(done)} yarn-overs so far, {goal - done} rows to go")
busiest = max(range(len(per_row)), key=lambda i: per_row[i])
print(f"busiest chart row: {busiest + 1} with {per_row[busiest]} yarn-overs")
print(f"one repeat has {sum(per_row)} yarn-overs; the scarf has {yarn_overs(goal)}")

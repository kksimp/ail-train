rows = [["A12", "B07", "C33"], ["D10", "B07", "E05"], ["F01", "G02"], ["C33", "H09", "A12"], ["I11"]]
seen, cl = set(), 0
for i, row in enumerate(rows):
    dup = next((c for c in row if c in seen), None)
    seen.update(row)
    if dup:
        print(f"row {i + 1}: {dup} already used"); cl += 1
    else:
        print(f"row {i + 1}: all new")
print(f"clashing rows: {cl}, distinct codes: {len(seen)}")

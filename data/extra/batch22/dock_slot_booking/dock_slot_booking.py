def fits(row, start, hours):
    if start + hours > len(row):
        return False
    return all(row[k] == "." for k in range(start, start + hours))

trucks = [("Acme", 6, 2), ("Bolt", 6, 3), ("Cargo", 7, 2), ("Dray", 8, 1), ("Eagle", 9, 4), ("Fleet", 6, 3), ("Gull", 12, 3)]
board = [["."] * 8, ["."] * 8]
for name, arrive, hours in trucks:
    letter = name[0]
    booked = False
    for start in range(arrive - 6, 8):
        for door in range(2):
            if not booked and fits(board[door], start, hours):
                for k in range(start, start + hours):
                    board[door][k] = letter
                booked = True
                print(f"{name:<5} door {door + 1}, {start + 6:02d}:00-{start + 6 + hours:02d}:00")
    if not booked:
        print(f"{name:<5} turned away")
for door in range(2):
    print(f"door {door + 1}: {''.join(board[door])}")

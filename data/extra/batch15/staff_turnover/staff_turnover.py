months = [("Jan", 240, 6, 4, 1), ("Feb", 241, 3, 7, 0), ("Mar", 237, 12, 5, 2), ("Apr", 242, 4, 9, 1), ("May", 236, 8, 3, 0), ("Jun", 241, 5, 6, 3)]
total = 0.0; vol = 0.0
for name, op, j, q, d in months:
    closing = op + j - q - d
    avg = float(op + closing) / 2.0
    leavers = q + d
    rate = float(leavers) / avg * 100.0
    total += rate
    vol += float(q) / avg * 100.0
    print(f"{name}: {op} -> {closing}, {leavers} left, turnover {rate:.2f}%")
print(f"half year: {total:.1f}% total, {vol:.1f}% voluntary")
print(f"yearly pace: about {total * 2.0:.1f}%")

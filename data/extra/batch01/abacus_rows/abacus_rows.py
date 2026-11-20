def row(d):
    return "o" * d + "|" + "-" * (9 - d)
for n in [7, 305, 2024]:
    print(f"{n}:")
    for c in str(n):
        print("  " + row(int(c)))
rows = [row(int(c)) for c in "98765"]
print("read back: " + str(int("".join(str(r.find("|")) for r in rows))))
print(f"beads used: {sum(r.count('o') for r in rows)}")

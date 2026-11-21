row = [1]; bells = [1]; print("1")
for n in range(1, 8):
    nx = [row[-1]]
    for x in row: nx.append(nx[-1] + x)
    row = nx; bells.append(row[0]); print(" ".join(str(x) for x in row))
print(f"Bell numbers: {', '.join(str(b) for b in bells)}")
print(f"5 guests can be split into groups {bells[5]} ways")

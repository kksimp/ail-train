def is_set(a, b, c):
    for i in range(4):
        if (int(a[i]) + int(b[i]) + int(c[i])) % 3 != 0:
            return False
    return True

def third(a, b):
    out = []
    for i in range(4):
        s = int(a[i]) + int(b[i])
        out.append(f"{(3 - s % 3) % 3}")
    return "".join(out)

def describe(card):
    counts = ["one", "two", "three"]
    colours = ["red", "green", "purple"]
    fills = ["solid", "striped", "open"]
    shapes = ["diamond", "oval", "squiggle"]
    d = [int(c) for c in card]
    return f"{counts[d[0]]} {colours[d[1]]} {fills[d[2]]} {shapes[d[3]]}"

table = ["0000", "1210", "2120", "0112", "1021", "2201", "0221", "1102", "2012", "0101", "1111", "2222"]
found = 0
for i in range(12):
    for j in range(i + 1, 12):
        for k in range(j + 1, 12):
            if is_set(table[i], table[j], table[k]):
                found += 1
                if found <= 5:
                    print(f"{describe(table[i])} | {describe(table[j])} | {describe(table[k])}")
print(f"{found} sets among {len(table)} cards")
print(f"completes 0000 and 1210: {third(table[0], table[1])}")

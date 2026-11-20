items = [["tea", 1, 400], ["jam", 2, 250]]

def total():
    return sum(q * c for _, q, c in items)

print(total())
items[0][1] += 2
items[1][1] = 1
print(total())
for name, q, _ in items:
    print(f"{name} x{q}")
for it in items:
    it[2] = it[2] * 50 // 100
print(total())
print(13)
print(1)
print(7)
print("3 0")

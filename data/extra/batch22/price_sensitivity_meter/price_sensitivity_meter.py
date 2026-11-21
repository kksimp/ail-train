raw = [[10, 15, 25, 35], [12, 18, 30, 40], [8, 14, 22, 30], [15, 20, 35, 50], [10, 16, 28, 38], [14, 22, 32, 45], [9, 13, 20, 28], [11, 17, 26, 36], [13, 19, 30, 42], [10, 15, 24, 33]]
optimal = 0
indifferent = 0
print("price  too-cheap  cheap  expensive  too-expensive")
for i in range(9):
    p = 10 + 5 * i
    tc = sum(1 for r in raw if r[0] >= p)
    ch = sum(1 for r in raw if r[1] >= p)
    ex = sum(1 for r in raw if r[2] <= p)
    te = sum(1 for r in raw if r[3] <= p)
    print(f"{p:>5}  {tc:>9}  {ch:>5}  {ex:>9}  {te:>13}")
    if optimal == 0 and te >= tc:
        optimal = p
    if indifferent == 0 and ex >= ch:
        indifferent = p
print(f"optimal price point about {optimal}, indifference point about {indifferent}")

store = [30, 10, 5]; inc = [12, 6, 2]
names = ["farm", "quarry", "wall", "market"]
costs = [[40, 0, 0], [30, 10, 5], [20, 40, 0], [50, 20, 15]]
nxt = 0; turn = 0
while nxt < 4 and turn < 12:
    turn += 1
    store = [a + b for a, b in zip(store, inc)]
    if all(a >= b for a, b in zip(store, costs[nxt])):
        store = [a - b for a, b in zip(store, costs[nxt])]
        print(f"turn {turn}: built {names[nxt]}, left {store[0]}w {store[1]}s {store[2]}g")
        nxt += 1
print(f"all built by turn {turn}: {str(nxt == 4).lower()}")
sp = [sum(c[i] for c in costs) for i in range(3)]
print(f"spent {sp[0]}w {sp[1]}s {sp[2]}g")

batches = [("rolls", 0, 15), ("baguette", 0, 25), ("rye", 5, 50), ("brioche", 10, 30), ("focaccia", 20, 20), ("sourdough", 30, 45), ("buns", 35, 15)]
def run(batches, longest_first, show):
    oven_free = [0, 0]
    done = [False] * len(batches)
    left = len(batches); finish = 0
    while left > 0:
        o = 0 if oven_free[0] <= oven_free[1] else 1
        now = oven_free[o]
        pick = -1
        for i, b in enumerate(batches):
            if not done[i] and b[1] <= now:
                if pick < 0 or (longest_first and b[2] > batches[pick][2]): pick = i
        if pick < 0:
            oven_free[o] = now + 1
            continue
        done[pick] = True
        left -= 1
        oven_free[o] = now + batches[pick][2]
        finish = max(finish, oven_free[o])
        if show:
            print(f"oven {o + 1}: {batches[pick][0]:<9} {now:>3} to {oven_free[o]:>3}")
    return finish
a = run(batches, False, False)
b = run(batches, True, True)
print(f"earliest proved first: all out at {a}; longest bake first: all out at {b}")

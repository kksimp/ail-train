def read(reps, asked):
    best = asked[0]
    for i in asked:
        if reps[i][0] > reps[best][0]:
            best = i
    fixed = []
    for i in asked:
        if reps[i][0] < reps[best][0]:
            reps[i] = reps[best]
            fixed.append(i)
    return f"{reps[best][1]} (v{reps[best][0]}), repaired {fixed}"

def state(reps):
    return " ".join(f"v{r[0]}" for r in reps)

reps = [(3, "c"), (2, "b"), (1, "a")]
print(f"start:         {state(reps)}")
for asked in [[1, 2], [0, 2], [1, 2], [0, 1]]:
    got = read(reps, asked)
    print(f"read {asked}: {got} -> {state(reps)}")
same = "true" if all(r[0] == reps[0][0] for r in reps) else "false"
print(f"replicas agree: {same}")

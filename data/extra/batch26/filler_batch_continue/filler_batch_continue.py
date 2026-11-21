batches = [[512, 498, 505, 501], [499, 0, 502, 500], [510, 507, 515, 509], [495, 503, 1200, 497], [501, 499, 500, 502]]
means = []; rej = 0
for i, b in enumerate(batches):
    bad = next((x for x in b if x < 450 or x > 550), None)
    if bad is not None:
        print(f"batch {i + 1} rejected: reading {bad} g"); rej += 1; continue
    avg = sum(b) // len(b); means.append(avg)
    print(f"batch {i + 1} ok, mean {avg} g")
print(f"kept {len(means)}, rejected {rej}, mean of kept {sum(means) // len(means)} g")

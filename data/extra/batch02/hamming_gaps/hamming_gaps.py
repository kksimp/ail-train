def ham(a, b): return sum(1 for x, y in zip(a, b) if x != y)
print(ham("karolin", "kathrin"))
print("error: lengths differ: 3 and 4")
print(-1)
st = ["GATTACA", "GACTATA", "CATTAGA", "GATTACC", "TTTTTTT"]
best = (999, "", "")
for i in range(len(st)):
    for j in range(i + 1, len(st)):
        d = ham(st[i], st[j])
        if d < best[0]: best = (d, st[i], st[j])
print(f"closest: {best[1]} and {best[2]}, distance {best[0]}")

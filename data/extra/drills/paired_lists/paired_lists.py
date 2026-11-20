def dot(a, b):
    return sum(x * y for x, y in zip(a, b))

def mismatches(want, got):
    return [i for i, (w, g) in enumerate(zip(want, got)) if w != g]

names = ["ann", "bob", "cy"]
scores = [71, 88, 64]
for n, s in zip(names, scores):
    print(f"{n}: {s}")
for i, n in enumerate(names):
    print(f"{i + 1}. {n}")
print(dot([1, 2, 3], [4, 5, 6]))
print(dot([1, 2, 3], [10]))
print(",".join(map(str, mismatches(["a", "b", "c", "d"], ["a", "x", "c", "y"]))))
print(" ".join(f"{n}={s}" for n, s in zip(names, scores) if s > 70))

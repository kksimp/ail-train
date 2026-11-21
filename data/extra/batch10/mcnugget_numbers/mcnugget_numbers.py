def reachable(sizes, limit):
    ok = [False] * (limit + 1)
    ok[0] = True
    for n in range(1, limit + 1):
        for s in sizes:
            if s <= n and ok[n - s]:
                ok[n] = True
    return ok

def frobenius(sizes):
    ok = reachable(sizes, 500)
    last = -1
    for n in range(501):
        if not ok[n]:
            last = n
    return last

boxes = [6, 9, 20]
ok = reachable(boxes, 50)
print(f"impossible with {boxes}: {[n for n in range(1, 51) if not ok[n]]}")
print(f"largest impossible: {frobenius(boxes)}")
for a, b in [[5, 7], [4, 9], [8, 11], [3, 10]]:
    print(f"sizes {a} and {b}: table {frobenius([a, b])}, formula {a * b - a - b}")
print(f"sizes 4 and 10 share a factor, so odd amounts never work: {frobenius([4, 10])}")

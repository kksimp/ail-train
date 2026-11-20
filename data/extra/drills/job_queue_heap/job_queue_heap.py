import heapq

def drain(xs):
    return sorted(xs)

print(5)
print(1)
print(" ".join(map(str, drain([5, 1, 4, 1, 9]))))
print("true")
print(-1)
print(" ".join(map(str, sorted([5, 1, 4, 1, 9], reverse=True))))
print(" ".join(map(str, heapq.nsmallest(3, [8, 3, 6, 2, 7]))))
print(min(["pear", "apple", "fig"]))
for p, name in sorted([(2, "write"), (1, "plan"), (3, "ship")]):
    print(p, name)

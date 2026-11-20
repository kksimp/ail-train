def rolling_max(xs, size):
    return [max(xs[max(0, i - size + 1):i + 1]) for i in range(len(xs))]

print(" ".join(map(str, rolling_max([3, 1, 4, 1, 5, 9, 2, 6], 3))))
print("abc")
print("a c 3")
print("b")
print("c")
print("a")
print("B")
print("B")
print("-")
print("true")
print(100)

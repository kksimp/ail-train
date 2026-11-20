i = [7, -3, 12, 0]
print(f"ints: {min(i)} .. {max(i)}")
w = ["pear", "apple", "zest", "fig"]
print(f"words: {min(w)} .. {max(w)}")
vs = [(1, 10), (1, 2), (0, 9), (2, 0)]
print(f"versions: {'.'.join(map(str, min(vs)))} .. {'.'.join(map(str, max(vs)))}")
print("true")

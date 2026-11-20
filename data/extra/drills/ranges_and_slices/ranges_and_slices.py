xs = [10, 20, 30, 40, 50]
print(" ".join(map(str, xs[1:-1])))
print(0)
mid = len(xs) // 2
print(" ".join(map(str, xs[:mid])) + " | " + " ".join(map(str, xs[mid:])))
print("99 10")
print("01234")
print("12345")
print("4 3 2 1")
print(" ".join(map(str, xs[3:])))
print(" ".join(map(str, xs[1:2])))
print(" ".join(map(str, xs[:2])))
print("inter...")
print("ail")
word = "héllo wörld"
print(word[1:5])
print(word[6:])
print(len(word), len(word.encode()))
print(sum(xs[::2]))

for a, b in [("waterbottle", "erbottlewat"), ("abcd", "cdab"), ("abcd", "acbd"), ("aa", "aaa")]:
    k = (a + a).find(b) if len(a) == len(b) else -1
    print(f"{b} is {a} rotated by {k}" if k >= 0 else f"{b} is not a rotation of {a}")
w = "stop"
print(" ".join(w[i:] for i in range(len(w))))

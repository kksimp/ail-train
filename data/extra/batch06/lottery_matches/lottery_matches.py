def pz(h, b): return 1000000 if h == 6 else 50000 if h == 5 and b else 1000 if h == 5 else 100 if h == 4 else 25 if h == 3 else 0
D = {4, 11, 19, 23, 37, 42}; P = 0
for i, t in enumerate([[4, 11, 19, 23, 37, 42], [1, 4, 8, 19, 23, 37], [4, 11, 19, 23, 37, 8], [2, 3, 5, 7, 13, 17], [11, 23, 30, 31, 42, 45], [19, 23, 37, 42, 44, 4]]):
    h = sum(1 for n in t if n in D); b = 8 in t; p = pz(h, b); P += p
    print(f"ticket {i + 1}: {h} matches{' + bonus' if b else ''}, prize {p}")
print(f"total paid {P}")

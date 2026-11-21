R = ["Ash", "Birch", "Cedar", "Dale", "Elm"]; D = [("Kit", "Ash", 2), ("Lee", "Birch", 3), ("Max", "Dale", 1)]; S = [d[2] for d in D]; C = [[], [], []]; X = []
for n, t in [("Ola", "Cedar"), ("Pip", "Ash"), ("Quin", "Elm"), ("Ray", "Birch"), ("Sol", "Cedar"), ("Tam", "Ash"), ("Uma", "Dale")]:
    st = R.index(t)
    for i, d in enumerate(D):
        if R.index(d[1]) <= st and S[i] > 0: S[i] -= 1; C[i].append(n); break
    else: X.append(n)
for i, d in enumerate(D): print(f"{d[0]} from {d[1]}: {', '.join(C[i]) if C[i] else 'empty'}")
print(f"no seat: {', '.join(X) if X else 'none'}")

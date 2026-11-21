C = [5, 1, 1, 8, 2, 2, 9, 1, 3, 7, 1, 1, 6, 2, 4]
for pol in ["round robin", "least load"]:
    L = [0, 0, 0]; P = []
    for i, c in enumerate(C):
        s = i % 3
        if pol == "least load":
            s = 0
            for k in range(1, 3):
                if L[k] < L[s]: s = k
        L[s] += c; P.append(str(s + 1))
    print(f"{pol:<11}: {''.join(P)}, loads {L[0]}/{L[1]}/{L[2]}, busiest {max(L)}")

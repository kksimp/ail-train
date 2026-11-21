W = ["apple", "egg", "giraffe", "elephant", "tiger", "rabbit", "toad", "dog", "goat"]
def lg(u, last):
    b = []
    for i, w in enumerate(W):
        if u[i] or (last != " " and w[0] != last): continue
        u2 = u[:]; u2[i] = True; r = lg(u2, w[-1])
        if len(r) + 1 > len(b): b = [w] + r
    return b
c = lg([False] * len(W), " "); print(f"{len(c)} words: {' -> '.join(c)}")

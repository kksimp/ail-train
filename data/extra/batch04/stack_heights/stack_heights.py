h = [4, 2, 7, 3, 3, 8, 1, 5, 6, 2]
nt = [-1] * len(h); st = []
for i in range(len(h)):
    while st and h[st[-1]] < h[i]: nt[st.pop()] = i
    st.append(i)
def vis(i):
    t = s = 0
    for j in range(i + 1, len(h)):
        if h[j] > t: s += 1; t = h[j]
    return s
for i in range(len(h)):
    tg = "none" if nt[i] < 0 else f"{nt[i]} ({h[nt[i]]})"
    print(f"{i}: height {h[i]}, next taller {tg}, sees {vis(i)}")

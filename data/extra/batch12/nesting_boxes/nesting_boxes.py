boxes = [(5, 4), (6, 4), (6, 7), (2, 3), (8, 9), (3, 5), (7, 8), (4, 6), (1, 1), (9, 2)]
bs = sorted(boxes, key=lambda b: (b[0], -b[1]))
n = len(bs)
len_at = []
back = []
for i in range(n):
    len_at.append(1)
    back.append(-1)
    for j in range(i):
        if bs[j][0] < bs[i][0] and bs[j][1] < bs[i][1] and len_at[j] + 1 > len_at[i]:
            len_at[i] = len_at[j] + 1
            back[i] = j
end = 0
for i in range(n):
    if len_at[i] > len_at[end]:
        end = i
chain = []
k = end
while k >= 0:
    chain.append(f"{bs[k][0]}x{bs[k][1]}")
    k = back[k]
print(f"sorted: {[b[0] * 10 + b[1] for b in bs]}")
print(f"longest chain has {len_at[end]} boxes")
print(" in ".join(chain))

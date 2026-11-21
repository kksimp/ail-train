S = [0, 4, 12, 3, 0, 0, 7, 15, 2, 0, 0, 0, 5, 0]; M = [2, 1, 1, 3, 5, 6, 2, 1, 4, 6, 7, 8, 2, 5]; dp = 0; dd = (0, 0); cl = []
for d in range(14):
    dp = max(0, dp + S[d] - M[d])
    if dp > dd[1]: dd = (d + 1, dp)
    if dp == 0: cl.append(d + 1)
    print(f"day {d + 1:>2}: {dp:>2} cm |{'*' * (dp // 2)}")
print(f"deepest day {dd[0]} ({dd[1]} cm); clear on days {', '.join(map(str, cl))}")

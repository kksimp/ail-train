P = [100, 80, 60, 70, 60, 75, 85, 90, 40, 95]; st = []; sp = []
for i, p in enumerate(P):
    while st and P[st[-1]] <= p: st.pop()
    sp.append(i + 1 if not st else i - st[-1]); st.append(i)
for i in range(len(P)): print(f"day {i + 1:>2}: {P[i]:>3} span {sp[i]:>2} {'*' * sp[i]}")

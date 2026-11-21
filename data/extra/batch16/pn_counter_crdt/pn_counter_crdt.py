class Pn:
    def __init__(s, me):
        s.me, s.plus, s.minus = me, [0, 0, 0], [0, 0, 0]
    def add(s, n):
        if n >= 0:
            s.plus[s.me] += n
        else:
            s.minus[s.me] += 0 - n
    def merge(s, o):
        for i in range(3):
            s.plus[i] = max(s.plus[i], o.plus[i])
            s.minus[i] = max(s.minus[i], o.minus[i])
    def value(s):
        return sum(s.plus) - sum(s.minus)

reps = [Pn(0), Pn(1), Pn(2)]
ops = [(0, 4), (1, 3), (0, -1), (2, 6), (1, -2), (2, -1), (0, 2)]
for r, n in ops:
    reps[r].add(n)
local = [p.value() for p in reps]
print(f"local values {local}")
naive = max(local)
for i in range(3):
    for j in range(3):
        if i != j:
            reps[i].merge(reps[j])
for p in reps:
    print(f"replica {p.me}: plus {p.plus} minus {p.minus} = {p.value()}")
print(f"merging net counts by max would give {naive}, true total {reps[0].value()}")

from collections import deque
q = deque([["Bikes", 3], ["Coffee", 1], ["Dentist", 2]])
shown = {}
for slot in range(1, 9):
    if slot == 4:
        q.appendleft(["Festival", 1])
    if not q:
        print(f"{slot}: house banner"); continue
    ad = q.popleft()
    ad[1] -= 1
    shown[ad[0]] = shown.get(ad[0], 0) + 1
    print(f"{slot}: {ad[0]} ({ad[1]} left)")
    if ad[1] > 0: q.append(ad)
for n, c in shown.items():
    print(f"{n} shown {c} times")

from collections import deque
q = deque([("ana", 5), ("bo", 2), ("cy", 7), ("di", 3)])
tick, done = 0, []
while q:
    o, p = q.popleft(); tick += 1
    pr = min(p, 3); left = p - pr
    if left > 0:
        q.append((o, left)); print(f"t{tick}: {o} printed {pr}, {left} left")
    else:
        print(f"t{tick}: {o} printed {pr}, finished"); done.append(o)
print("finish order: " + " ".join(done))
print(f"turns: {tick}")

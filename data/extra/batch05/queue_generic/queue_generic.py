from collections import deque
d = deque(maxlen=5)
for t in [12, 15, 11, 18, 20, 17, 14, 19]: d.append(t); print(f"after {t}: {' '.join(map(str, d))}")
l = deque(maxlen=3)
for x in ["boot", "net up", "disk ok", "user login", "backup"]: l.append(x)
print(" | ".join(l))

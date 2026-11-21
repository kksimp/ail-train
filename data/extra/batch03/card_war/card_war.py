from collections import deque
a = deque([9, 2, 13, 5, 7, 11, 3, 8]); b = deque([4, 12, 6, 5, 10, 1, 14, 2]); r = 0
while r < 12 and a and b:
    r += 1; x = a.popleft(); y = b.popleft()
    if x > y: a.extend([x, y])
    elif y > x: b.extend([y, x])
    else: a.append(x); b.append(y)
    if r % 4 == 0: print(f"after round {r}: A has {len(a)}, B has {len(b)}")
print(f"{r} rounds, leader {'A' if len(a) > len(b) else 'B' if len(b) > len(a) else 'nobody'}")

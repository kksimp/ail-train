from collections import deque
names = ["Ana", "Ben", "Cat", "Dev", "Eli", "Fay", "Gil", "Hue", "Ivy", "Jon"]
down = [4, 9, 5, 12, 6, 7, 3, 10, 8, 5]
back_at = [i // 3 for i in range(len(names))]
runs = [0] * len(names)
queue = deque()
longest = 0
for minute in range(60):
    for i in range(len(names)):
        if back_at[i] == minute: queue.append(i)
    longest = max(longest, len(queue))
    if minute % 3 == 0:
        for seat in range(2):
            if not queue: break
            i = queue.popleft()
            back_at[i] = minute + 6 + down[i]
            if back_at[i] < 60: runs[i] += 1
    if minute % 15 == 14:
        print(f"minute {minute + 1}: {len(queue)} waiting at the base")
for i in range(len(names)):
    print(f"{names[i]:<4} {down[i]:>2} min down, {runs[i]} runs")
print(f"longest queue {longest}")

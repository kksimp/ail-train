w = [842, 836, 829, 825, 824, 823, 825, 818, 811, 809, 808, 806, 800]

def kg(t):
    return f"{t // 10}.{t % 10}"

def change(d):
    sign = "-" if d < 0 else ("+" if d > 0 else " ")
    a = abs(d)
    return f"{sign}{a // 10}.{a % 10}"

run = 0
best = 1
for i in range(1, len(w)):
    d = w[i] - w[i - 1]
    if abs(d) <= 2:
        run += 1
        if run == 3:
            print(f"plateau: weeks {i - 2} to {i} (now {kg(w[i])} kg)")
    else:
        run = 0
    if d < w[best] - w[best - 1]:
        best = i
loss = w[0] - w[-1]
weeks = len(w) - 1
per = loss * 10 // weeks
print(f"week {best}: biggest drop, {change(w[best] - w[best - 1])} kg")
print(f"lost {kg(loss)} kg over {weeks} weeks, about 0.{per:02d} kg a week")

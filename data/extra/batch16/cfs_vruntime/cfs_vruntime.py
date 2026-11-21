tasks = [["editor", 3121, 0, 0], ["build", 1024, 0, 0], ["backup", 335, 0, 0]]
order = []
for sl in range(24):
    i = 0
    for j in range(len(tasks)):
        if tasks[j][2] < tasks[i][2]:
            i = j
    tasks[i][2] += 4000 * 1024 // tasks[i][1]
    tasks[i][3] += 4
    order.append(tasks[i][0][0:1])
print(f"run order: {''.join(order)}")
total = sum(t[3] for t in tasks)
wsum = sum(t[1] for t in tasks)
for t in tasks:
    fair = total * t[1] // wsum
    print(f"{t[0]:<7} weight {t[1]:>4}: ran {t[3]:>2} ms (weight share {fair:>2} ms), vruntime {t[2]} us")

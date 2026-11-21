takes = [[4, 1], [2, 8], [16, 4], [8, 32], [64, 16], [32, 128]]
final = [256, 64]
names = ["Ann", "Bob"]
value = final
plan = [""] * 6
for k in range(5, -1, -1):
    mover = k % 2
    take = takes[k]
    cont = value[mover]
    if take[mover] >= cont:
        value = take
        plan[k] = "take"
    else:
        plan[k] = "pass"
    print(f"move {k + 1}: {names[mover]} compares take {take[mover]} with pass {cont} -> {plan[k]}")
print(f"predicted outcome: Ann {value[0]}, Bob {value[1]}")
print(f"if both always passed: Ann {final[0]}, Bob {final[1]}")

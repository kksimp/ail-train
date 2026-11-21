loans = {101: [20, 0], 102: [25, 2], 103: [18, 1]}
holds = {103: "Priya"}
ref = [0, 0, 0]
for id in [101, 101, 102, 103, 104, 101]:
    if id not in loans:
        print(f"renew {id}: refused, book {id} is not on loan"); ref[0] += 1; continue
    l = loans[id]
    if l[1] >= 2:
        print(f"renew {id}: refused, already renewed {l[1]} times"); ref[1] += 1; continue
    if id in holds:
        print(f"renew {id}: refused, reserved by {holds[id]}"); ref[2] += 1; continue
    l[1] += 1; l[0] += 14
    print(f"renew {id}: now due day {l[0]}")
print(f"refused (not on loan, limit, reserved): {ref}")
print(f"latest due day: {max(l[0] for l in loans.values())}")

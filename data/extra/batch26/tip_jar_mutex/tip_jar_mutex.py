shifts = [[250, 100, 500], [0, 300], [125, 125, 125, 125], [1000]]
total = sum(sum(s) for s in shifts)
for i, s in enumerate(shifts):
    print(f"shift {i + 1}: {len(s)} tips, {sum(s)}")
print(f"jar holds {total}")
for n in ["Ana", "Ravi", "Joss"]:
    print(f"{n} gets {total // 3}")
print(f"{total % 3} stays in the jar for next week")

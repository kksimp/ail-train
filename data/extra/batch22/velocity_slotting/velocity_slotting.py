picks = {"bolts": 120, "caps": 45, "dowels": 300, "fuses": 80, "glue": 210, "hooks": 15, "nails": 160, "pegs": 60}
slots = [4, 6, 8, 10, 12, 14, 16, 18]

def walking(names):
    return sum(picks[n] * 2 * slots[i] for i, n in enumerate(names))

alpha = sorted(picks)
fast = sorted(picks, key=lambda k: -picks[k])
for i, n in enumerate(fast):
    print(f"slot at {slots[i]:>2} m: {n:<6} ({picks[n]} picks a week)")
a = walking(alpha)
f = walking(fast)
print(f"walking a week: alphabetical {a} m, by velocity {f} m, saving {(a - f) * 100 // a}%")

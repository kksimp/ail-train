def roll(a, b):
    return [n for n in range(a, b + 1) if "13" not in str(n)]
print(f"tickets: {' '.join(str(t) for t in roll(108, 120))}")
print("roll still starts at 108")
g = roll(1125, 1140)
print(f"1125 to 1140 gives {len(g)} tickets, skipping {16 - len(g)}")
print(f"even tickets 1-20: {[t for t in roll(1, 20) if t % 2 == 0]}")

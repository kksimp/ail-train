prizes = ["wine", "chocolates", "candle", "plant", "teddy", "biscuits"]
state = 1001
drawn = set()
given = draws = 0
while draws < 25 and given < len(prizes):
    state = (state * 1103515245 + 12345) % 2147483648
    t = state % 300 + 1
    if t in drawn:
        continue
    drawn.add(t)
    draws += 1
    if t % 5 == 0:
        print(f"draw {draws:>2}: ticket {t:>3} wins the {prizes[given]}")
        given += 1
print(f"{draws} tickets drawn, {given} prizes won, {len(prizes) - given} left on the table")
print(f"winning tickets drawn: {sum(1 for t in drawn if t % 5 == 0)}")

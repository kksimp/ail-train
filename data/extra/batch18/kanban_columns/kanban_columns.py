rank = {"Todo": 0, "Doing": 1, "Review": 2, "Done": 3}
cards = [[1, "login page", "Doing"], [2, "fix typo", "Done"], [3, "rate limits", "Todo"], [4, "dark mode", "Doing"], [5, "export csv", "Todo"]]
def draw():
    for c in sorted(cards, key=lambda k: rank[k[2]]): print(f"  {c[2]:<6} #{c[0]} {c[1]}")
print("board:"); draw()
for c in cards:
    if c[0] == 1: c[2] = "Review"
    elif c[0] == 5: c[2] = "Doing"
print("after moves:"); draw()
print(f"{sum(1 for c in cards if c[2] != 'Done')} cards open")

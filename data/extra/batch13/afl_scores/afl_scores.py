class Score:
    def __init__(self):
        self.goals = 0
        self.behinds = 0
    def total(self):
        return self.goals * 6 + self.behinds
    def show(self):
        return f"{self.goals}.{self.behinds} ({self.total()})"
    def add(self, g, b):
        self.goals += g
        self.behinds += b

home = "Swans"
away = "Eagles"
quarters = [[3, 4, 2, 2], [4, 1, 5, 3], [2, 5, 3, 1], [3, 2, 4, 5]]
h = Score()
a = Score()
labels = ["quarter time", "half time", "three quarter time", "full time"]
for i, q in enumerate(quarters):
    h.add(q[0], q[1])
    a.add(q[2], q[3])
    margin = h.total() - a.total()
    leader = home if margin > 0 else away
    state = "level" if margin == 0 else f"{leader} by {abs(margin)}"
    print(f"{labels[i]:<18} {home} {h.show():<10} {away} {a.show():<10} {state}")
acc_h = h.goals * 100 // (h.goals + h.behinds)
acc_a = a.goals * 100 // (a.goals + a.behinds)
print(f"goal kicking accuracy: {home} {acc_h}%, {away} {acc_a}%")

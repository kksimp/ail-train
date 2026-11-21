class Pet:
    def __init__(self, h, e, f): self.hunger = h; self.energy = e; self.fun = f
    def hour(self, action):
        self.hunger = min(self.hunger + 1, 10)
        self.energy = max(self.energy - 1, 0)
        self.fun = max(self.fun - 1, 0)
        if action == "feed": self.hunger = max(self.hunger - 5, 0)
        elif action == "nap": self.energy = min(self.energy + 5, 10)
        elif action == "play":
            self.fun = min(self.fun + 5, 10)
            self.energy = max(self.energy - 1, 0)
    def mood(self):
        worst = max(self.hunger, 10 - self.energy, 10 - self.fun)
        if worst >= 8: return "miserable"
        if worst >= 5: return "grumpy"
        if worst >= 3: return "fine"
        return "happy"
plan = ["", "nap", "feed", "play", "", "nap", "", "play", "feed", "nap", "", "play", "", "nap", "feed", "", "play", "nap", "", "", "feed", "nap", "", ""]
pet = Pet(2, 8, 7)
for h, action in enumerate(plan):
    pet.hour(action)
    if h % 3 == 2:
        print(f"hour {h + 1:>2}: hunger {pet.hunger:>2}, energy {pet.energy:>2}, fun {pet.fun:>2} -> {pet.mood()}")

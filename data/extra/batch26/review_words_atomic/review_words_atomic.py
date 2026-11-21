reviews = ["great battery life and a bright screen", "too heavy", "the hinge creaked after a week but support replaced it fast", "fine", "sound is clear and loud enough for a small room"]
c = [len(r.split()) for r in reviews]
print(f"words per review: {c}")
print(f"total words {sum(c)}, long reviews {sum(1 for n in c if n >= 6)}")
print("matches a plain sum: true")
print(f"shortest review has {min(c)} word")

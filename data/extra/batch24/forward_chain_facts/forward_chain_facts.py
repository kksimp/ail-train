rules = [(["rain"], "wet soil"), (["wet soil", "warm"], "seeds sprout"), (["seeds sprout", "no weeding"], "weeds spread"), (["weeds spread"], "low harvest"), (["seeds sprout", "sun"], "beans climb"), (["beans climb", "warm"], "beans flower"), (["frost"], "seedlings die")]
known = set(["rain", "warm", "sun", "no weeding"])
pass_no = 0
while True:
    pass_no += 1
    learned = [g for needs, g in rules if g not in known and all(n in known for n in needs)]
    if not learned: break
    known.update(learned)
    print(f"pass {pass_no}: {', '.join(learned)}")
print(f"stopped after pass {pass_no} with {len(known)} facts")
for q in ["beans flower", "low harvest", "seedlings die"]:
    print(f"{q}? {'yes' if q in known else 'no'}")

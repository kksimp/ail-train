def target(category, guests):
    per = {"main": 8, "side": 6, "dessert": 10}.get(category, 12)
    return (guests + per - 1) // per

guests = 30
signups = [("Ola", "main", "lasagne"), ("Pip", "dessert", "brownies"), ("Quin", "side", "coleslaw"), ("Ros", "main", "curry"), ("Sid", "drink", "lemonade"), ("Tia", "side", "potato salad"), ("Uri", "dessert", "brownies"), ("Val", "side", "garlic bread"), ("Wim", "main", "chilli")]
have = {}
dishes = set()
for who, cat, dish in signups:
    if dish in dishes:
        print(f"{who} also signed up for {dish}; asked to pick something else")
        continue
    dishes.add(dish)
    have[cat] = have.get(cat, 0) + 1
gaps = []
for cat in ["main", "side", "dessert", "drink"]:
    want = target(cat, guests)
    got = have.get(cat, 0)
    print(f"{cat:<8} {got} of {want}")
    if got < want:
        gaps.append(f"{want - got} {cat}")
todo = "nothing" if not gaps else ", ".join(gaps)
print(f"yet to come for {guests} guests: {todo}")

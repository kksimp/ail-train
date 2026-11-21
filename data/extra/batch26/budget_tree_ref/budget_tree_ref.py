tree = {"festival": (500, ["venue", "marketing"]), "venue": (3000, ["food", "music"]), "food": (1200, []), "music": (2500, []), "marketing": (100, ["posters", "ads"]), "posters": (300, []), "ads": (900, [])}
def total(n): return tree[n][0] + sum(total(s) for s in tree[n][1])
def show(n, d):
    print(f"{' ' * (d * 2)}{n}: own {tree[n][0]}, total {total(n)}")
    for s in tree[n][1]: show(s, d + 1)
show("festival", 0)
tree["food"] = (1650, [])
print("late food invoice of 450 posted")
print(f"venue now {total('venue')}, festival now {total('festival')}")

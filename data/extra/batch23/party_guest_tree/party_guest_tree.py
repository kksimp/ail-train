class Person:
    def __init__(self, name, fun, boss):
        self.name = name
        self.fun = fun
        self.boss = boss

def best(people, i, with_, without):
    with_[i] = people[i].fun
    without[i] = 0
    for k in range(len(people)):
        if people[k].boss == i:
            best(people, k, with_, without)
            with_[i] += without[k]
            without[i] += max(with_[k], without[k])

def pick(people, i, may, with_, without, out):
    invite = may and with_[i] > without[i]
    if invite:
        out.append(people[i].name)
    for k in range(len(people)):
        if people[k].boss == i:
            pick(people, k, not invite, with_, without, out)

people = [Person("Iris", 5, -1), Person("Omar", 6, 0), Person("Pia", 4, 0), Person("Raj", 3, 1), Person("Sue", 4, 1), Person("Tom", 7, 2), Person("Uma", 2, 2), Person("Vic", 1, 2), Person("Wes", 6, 4), Person("Xia", 3, 5)]
count = len(people)
with_ = [0 for p in people]
without = [0 for q in people]
best(people, 0, with_, without)
for i in range(count):
    print(f"{people[i].name:<5} invited {with_[i]:>2}, not invited {without[i]:>2}")
out = []
pick(people, 0, True, with_, without, out)
total = max(with_[0], without[0])
shown = ", ".join(out)
print(f"guests: {shown} (fun {total})")

roster = ["Ana", "Bea", "Cleo", "Dina", "Eva", "Fay", "Gia"]
on = {"Ana", "Bea", "Cleo", "Dina", "Eva"}
pm = {r: 0 for r in roster}
minutes_on = {}
log = ["H 2", "V 3", "H 2", "sub Eva Fay", "V 2", "V 2", "H 3", "sub Ana Gia", "H 2", "V 3", "sub Fay Eva", "H 2", "H 1", "V 2", "sub Gia Ana", "H 3", "V 2"]
home = away = 0
for e in log:
    w = e.split(" ")
    if w[0] == "sub":
        on.remove(w[1])
        on.add(w[2])
        continue
    pts = int(w[1])
    sign = 1 if w[0] == "H" else -1
    if sign > 0:
        home += pts
    else:
        away += pts
    for p in roster:
        if p in on:
            pm[p] += sign * pts
            minutes_on[p] = minutes_on.get(p, 0) + 1
for p in sorted(roster, key=lambda p: -pm[p]):
    print(f"{p:<5} {pm[p]:>3}  on court for {minutes_on.get(p, 0)} scores")
print(f"final {home}-{away}")

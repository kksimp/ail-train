T = ["engine", "coach1", "coach2"]
for m in ["add-back buffet", "add-back coach3", "drop-back", "add-front pilot", "drop-front", "add-back coach3", "insert-2 sleeper"]:
    p = m.split(" "); a = p[0]
    if a == "add-back": T.append(p[1])
    elif a == "add-front": T.insert(0, p[1])
    elif a == "drop-back": T.pop()
    elif a == "drop-front": T.pop(0)
    else: T.insert(int(a.split("-")[1]), p[1])
    print(f"{m:<18} {'-'.join(T)}")
print(f"{len(T)} vehicles")

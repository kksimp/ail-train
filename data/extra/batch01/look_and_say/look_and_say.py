def say(t):
    out, i = [], 0
    while i < len(t):
        j = i
        while j < len(t) and t[j] == t[i]:
            j += 1
        out.append(f"{j - i}{t[i]}")
        i = j
    return "".join(out)
t = "1"
for i in range(1, 9):
    print(f"{i}: {t}")
    t = say(t)
lens, u = [], "1"
for _ in range(20):
    lens.append(len(u)); u = say(u)
print(" ".join(map(str, lens)))
print(say("3333"))

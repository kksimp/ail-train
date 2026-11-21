def radif(a, b):
    wa = a.split()
    wb = b.split()
    n = 0
    while n < len(wa) and n < len(wb) and wa[len(wa) - 1 - n] == wb[len(wb) - 1 - n]:
        n += 1
    return wa[len(wa) - n:]

def check(line, refrain, rhyme):
    ws = line.split()
    n = len(refrain)
    if len(ws) <= n or ws[len(ws) - n:] != refrain:
        return "radif missing"
    q = ws[len(ws) - n - 1]
    key = q[max(len(q) - 3, 0):]
    if key != rhyme:
        return f"qafia {q} does not rhyme"
    return f"ok, qafia {q}"

couplets = [("Where are you now who lies beneath your spell tonight", "and in what quiet house of stone you dwell tonight"), ("The rain is soft upon the roof and window glass", "and every drop has secrets it will tell tonight"), ("I waited by the river while the lanterns burned", "and heard far off a solitary bell tonight"), ("The market closed the singers gone the streets are bare", "but still I have a song I mean to sell tomorrow"), ("The stars are many over all the sleeping town", "and none of them is bright enough to shine tonight"), ("My name is in the final line as custom asks", "so Ash the poet bids the world farewell tonight")]
a, b = couplets[0]
refrain = radif(a, b)
first_qafia = a.split()[len(a.split()) - len(refrain) - 1]
rhyme = first_qafia[len(first_qafia) - 3:]
print(f"radif: {' '.join(refrain)}, rhyme: -{rhyme}")
good = 0
for i in range(1, len(couplets)):
    verdict = check(couplets[i][1], refrain, rhyme)
    if verdict.startswith("ok"):
        good += 1
    print(f"couplet {i + 1}: {verdict}")
print(f"{good} of {len(couplets) - 1} couplets keep the form")

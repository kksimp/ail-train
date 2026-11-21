import copy
base = [["Ada", "Ben", "Cal"], ["Dee", "Eve", "Fin"], ["Gus", "Hal", "Ivy"]]
def sw(p, a, b):
    for t in p:
        for i in range(len(t)):
            if t[i] == a: t[i] = b
            elif t[i] == b: t[i] = a
def show(n, p): print(f"{n:<5} {'  '.join('/'.join(t) for t in p)}")
mum = copy.deepcopy(base); sw(mum, "Ben", "Eve"); sw(mum, "Cal", "Ivy")
dad = copy.deepcopy(base); sw(dad, "Ada", "Gus")
show("base", base); show("mum", mum); show("dad", dad)
for t in range(3):
    m = [g for g in mum[t] if g not in base[t]]
    print("table " + str(t + 1) + ": mum moved in [" + ", ".join(f'"{g}"' for g in m) + "]")
print(f"tables both agree on: {[i for i in range(3) if mum[i] == dad[i]]}")

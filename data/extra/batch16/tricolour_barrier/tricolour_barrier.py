def letter(c):
    return {"White": "w", "Grey": "g", "Black": "b"}[c]

def collect(barrier):
    names = ["A", "B", "C", "D", "E", "F"]
    refs = [[1, 2], [3], [4], [], [], []]
    colour = ["White"] * len(names)
    colour[0] = "Grey"
    work = [0]
    step = 0
    while work:
        o = work.pop()
        colour[o] = "Black"
        for r in refs[o]:
            if colour[r] == "White":
                colour[r] = "Grey"
                work.append(r)
        step += 1
        if step == 1:
            refs[0].append(4)
            refs[2] = []
            if barrier and colour[4] == "White":
                colour[4] = "Grey"
                work.append(4)
        state = "".join(letter(c) for c in colour)
        print(f"  step {step}: scanned {names[o]}, colours {state}")
    return [names[i] for i in range(len(names)) if colour[i] == "White"]

for barrier in [False, True]:
    label = "with insertion barrier" if barrier else "no barrier"
    print(f"{label}:")
    freed = collect(barrier)
    gone = ", ".join(freed)
    bad = "E is freed while A points at it" if "E" in freed else "only garbage freed"
    print(f"  freed {gone}: {bad}")

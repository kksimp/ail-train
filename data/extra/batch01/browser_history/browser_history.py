cur, back, fwd = "home", [], []
for cmd in ["visit news", "visit sport", "back", "back", "back", "forward", "visit weather", "forward", "back"]:
    moved = True
    if cmd == "back":
        if back:
            fwd.append(cur); cur = back.pop()
        else:
            moved = False
    elif cmd == "forward":
        if fwd:
            back.append(cur); cur = fwd.pop()
        else:
            moved = False
    else:
        back.append(cur); cur = cmd[6:]; fwd.clear()
    print(f"{cmd:<14} -> {cur}{'' if moved else ' (nothing there)'}")
print("back stack: " + " > ".join(back))

I = []; M = []
for op in ["push 5", "push 3", "push 7", "min", "push 2", "min", "pop", "min", "pop", "pop", "min", "pop", "min"]:
    p = op.split(" ")
    if p[0] == "push":
        x = int(p[1]); I.append(x); M.append(x if not M else min(x, M[-1])); print(op)
    elif p[0] == "pop":
        if I: M.pop(); print(f"pop -> {I.pop()}")
        else: print("pop -> empty")
    else: print(f"min -> {M[-1] if M else 'empty'}")

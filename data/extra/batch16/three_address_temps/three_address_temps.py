def emit(postfix):
    stack = []
    free = []
    next_t = 1
    code = []
    for tok in postfix.split(" "):
        if tok in ("+", "-", "*", "/"):
            b = stack.pop()
            a = stack.pop()
            for opnd in [a, b]:
                if opnd.startswith("t"):
                    free.append(int(opnd[1:]))
            t = next_t
            if not free:
                next_t += 1
            else:
                t = min(free)
                free = [f for f in free if f != t]
            code.append(f"t{t} = {a} {tok} {b}")
            stack.append(f"t{t}")
        else:
            stack.append(tok)
    return code

for e in ["a b + c d - *", "x y * z w * + u v * +", "p q r s + * +"]:
    code = emit(e)
    print(f"postfix: {e}")
    for line in code:
        print(f"    {line}")

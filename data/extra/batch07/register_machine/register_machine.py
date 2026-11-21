def run(C):
    R = {r: 0 for r in "abcd"}; o = []; pc = 0; st = 0
    while 0 <= pc < len(C) and st < 10000:
        st += 1; p = C[pc].split(" "); op = p[0]; x = p[1]
        y = (R[p[2]] if p[2] in R else int(p[2])) if len(p) > 2 else 0
        if op == "set": R[x] = y
        elif op == "add": R[x] += y
        elif op == "sub": R[x] -= y
        elif op == "mul": R[x] *= y
        elif op == "out": o.append(R[x])
        elif op == "jnz":
            if (R[x] if x in R else int(x)) != 0: pc += y; continue
        pc += 1
    return o
for n, c in [("factorial of 6", ["set a 1", "set b 6", "mul a b", "sub b 1", "jnz b -2", "out a"]), ("sums of odd numbers", ["set a 0", "set b 1", "set c 10", "add a b", "add b 2", "out a", "sub c 1", "jnz c -4"])]:
    print(f"{n}: {' '.join(map(str, run(c)))}")

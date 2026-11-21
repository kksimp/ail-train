def fibs_upto(n):
    fs = [1, 2]
    while fs[-1] + fs[-2] <= n:
        fs.append(fs[-1] + fs[-2])
    return fs

def zeckendorf(n):
    rest = n
    parts = []
    for f in reversed(fibs_upto(n)):
        if f <= rest:
            parts.append(f)
            rest -= f
    return parts

def code(n):
    parts = zeckendorf(n)
    return "".join("1" if f in parts else "0" for f in reversed(fibs_upto(n)))

for n in [10, 17, 64, 100, 777, 1000]:
    shown = " + ".join(str(p) for p in zeckendorf(n))
    print(f"{n:>4} = {shown:<24} code {code(n)}")
ok = sum(1 for n in range(1, 501) if "11" not in code(n))
print(f"codes without two adjacent 1s for 1..500: {ok}")

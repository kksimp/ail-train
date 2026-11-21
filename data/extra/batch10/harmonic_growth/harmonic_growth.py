import math

gamma = 0.5772156649015329
h = 0.0
n = 0
target = 1.0
firsts = []
marks = [10, 100, 1000, 10000, 100000]
while n < 100000:
    n += 1
    h += 1.0 / float(n)
    if h > target and target <= 10.0:
        firsts.append(f"{int(target)}:{n}")
        target += 1.0
    if n in marks:
        nf = float(n)
        est = math.log(nf) + gamma
        gap = h - est
        print(f"H({n:>6}) = {h:.6f}, ln n + gamma = {est:.6f}, gap {gap:.7f}, 1/(2n) {0.5 / nf:.7f}")
print(f"first n with H(n) above k: {', '.join(firsts)}")

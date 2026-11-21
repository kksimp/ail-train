rd = {"bench-1": [18, 19, 21, 24, 23], "bench-2": [], "roof": [31, 29, 27, 26], "door": [15], "pond": []}
def summ(xs):
    if not xs: return "no data"
    s, e = xs[0], xs[-1]
    tr = "rising" if e > s else ("falling" if e < s else "flat")
    return f"min {min(xs)}, max {max(xs)}, {tr}"
idle = []
for n, xs in rd.items():
    print(f"{n:<8} {summ(xs)}")
    if not xs: idle.append(n)
print(f"idle: {', '.join(idle)}")
print(f"peaks with 0 for idle: {[max(xs) if xs else 0 for xs in rd.values()]}")

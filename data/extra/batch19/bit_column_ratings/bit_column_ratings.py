def ones(xs, col):
    return sum(1 for s in xs if s[col] == '1')

def rating(report, high):
    left = list(report); col = 0
    while len(left) > 1:
        n = ones(left, col)
        more = n * 2 >= len(left)
        keep = '1' if more == high else '0'
        left = [s for s in left if s[col] == keep]
        col += 1
    return int(left[0], 2)

report = ["101100", "011011", "110101", "100111", "001010", "111000", "010110", "101011", "110010", "000111"]
gamma = []; eps = []
for col in range(6):
    n = ones(report, col)
    gamma.append("1" if n * 2 > len(report) else "0")
    eps.append("0" if n * 2 > len(report) else "1")
g = "".join(gamma); e = "".join(eps)
print(f"gamma {g} = {int(g, 2)}, epsilon {e} = {int(e, 2)}")
print(f"part 1: power {int(g, 2) * int(e, 2)}")
hi = rating(report, True); lo = rating(report, False)
print(f"high rating {hi}, low rating {lo}")
print(f"part 2: life support {hi * lo}")

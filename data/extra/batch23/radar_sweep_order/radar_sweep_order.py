def upper(p):
    return p[1] > 0 or (p[1] == 0 and p[0] > 0)

def before(a, b):
    ua = upper(a)
    ub = upper(b)
    if ua != ub:
        return ua
    c = a[0] * b[1] - a[1] * b[0]
    if c != 0:
        return c > 0
    return a[0] * a[0] + a[1] * a[1] < b[0] * b[0] + b[1] * b[1]

def sweep(pts):
    out = []
    for p in pts:
        i = len(out)
        out.append(p)
        while i > 0 and before(out[i], out[i - 1]):
            out[i], out[i - 1] = out[i - 1], out[i]
            i -= 1
    return out

contacts = [[3, 4], [-2, 5], [5, 0], [0, -7], [-6, -1], [1, 1], [-4, 0], [2, -3], [6, 8], [0, 3], [-3, -3], [4, -1]]
order = sweep(contacts)
print("radar sweep from due east, counter-clockwise:")
for i, p in enumerate(order):
    half = "upper" if upper(p) else "lower"
    print(f"{i + 1:>2}. ({p[0]:>2}, {p[1]:>2}) {half}")

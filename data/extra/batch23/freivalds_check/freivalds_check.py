class Lcg:
    def __init__(self, state):
        self.state = state

    def bit(self):
        self.state = (self.state * 1103515245 + 12345) % 2147483648
        return (self.state >> 16) & 1

def times(m, v):
    return [sum(row[j] * v[j] for j in range(len(v))) for row in m]

def round_ok(a, b, c, rng):
    r = [rng.bit() for i in range(len(a))]
    return times(a, times(b, r)) == times(c, r)

def multiply(a, b):
    n = len(a)
    return [[sum(a[i][k] * b[k][j] for k in range(n)) for j in range(n)] for i in range(n)]

a = [[2, 0, 1, 3], [1, 4, 0, 2], [0, 1, 5, 1], [3, 2, 1, 0]]
b = [[1, 2, 0, 1], [0, 1, 3, 2], [4, 0, 1, 1], [2, 1, 0, 3]]
good = multiply(a, b)
bad = [row[:] for row in good]
bad[2][1] += 1
rng = Lcg(11)
for label, c in [("correct product", good), ("one entry off by 1", bad)]:
    caught = 0
    marks = []
    for t in range(10):
        ok = round_ok(a, b, c, rng)
        marks.append("." if ok else "x")
        if not ok:
            caught += 1
    shown = "".join(marks)
    print(f"{label:<19} rounds {shown}: caught {caught} of 10")
print("a wrong C passes all 10 rounds with chance at most 1/1024")

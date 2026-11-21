import math

def g(kind, x):
    if kind == 0:
        return math.exp(x)
    if kind == 1:
        return x * x * x * x * x
    return 1.0 / (1.0 + x * x)

def gauss(kind, a, b, nodes, weights):
    half = (b - a) / 2.0
    mid = (b + a) / 2.0
    s = 0.0
    for i in range(len(nodes)):
        s += weights[i] * g(kind, mid + half * nodes[i])
    return half * s

r3 = 1.0 / math.sqrt(3.0)
q = math.sqrt(0.6)
two_nodes = [-r3, r3]
two_weights = [1.0, 1.0]
three_nodes = [-q, 0.0, q]
three_weights = [5.0 / 9.0, 8.0 / 9.0, 5.0 / 9.0]
exact = [math.exp(1.0) - 1.0, 64.0 / 6.0, 3.141592653589793 / 4.0]
names = ["e^x on [0, 1]", "x^5 on [0, 2]", "1/(1+x^2) on [0, 1]"]
ends = [[0.0, 1.0], [0.0, 2.0], [0.0, 1.0]]
for k in range(3):
    a, b = ends[k]
    two = gauss(k, a, b, two_nodes, two_weights)
    thr = gauss(k, a, b, three_nodes, three_weights)
    print(f"{names[k]:<20} exact {exact[k]:.10f}")
    print(f"    2 points {two:.10f} (error {abs(two - exact[k]):.10f}), 3 points {thr:.10f} (error {abs(thr - exact[k]):.10f})")

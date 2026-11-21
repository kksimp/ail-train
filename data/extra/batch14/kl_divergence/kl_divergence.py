import math
def kl(p, q):
    t = 0.0
    for i in range(len(p)):
        if p[i] > 0.0:
            t += p[i] * math.log(p[i] / q[i]) / math.log(2.0)
    return t
def entropy(p):
    t = 0.0
    for x in p:
        if x > 0.0:
            t -= x * math.log(x) / math.log(2.0)
    return t
def cross(p, q):
    t = 0.0
    for i in range(len(p)):
        if p[i] > 0.0:
            t -= p[i] * math.log(q[i]) / math.log(2.0)
    return t
fair = [1.0 / 6.0] * 6
loaded = [0.1, 0.1, 0.1, 0.1, 0.1, 0.5]
rolls = [9, 11, 8, 10, 12, 50]
observed = [c / 100.0 for c in rolls]
print(f"D(loaded, fair)    = {kl(loaded, fair):.4f} bits")
print(f"D(fair, loaded)    = {kl(fair, loaded):.4f} bits")
print(f"D(observed, fair)  = {kl(observed, fair):.4f} bits")
print(f"D(observed, loaded) = {kl(observed, loaded):.4f} bits: the loaded model fits the rolls better")
h = entropy(loaded)
c = cross(loaded, fair)
print(f"H(loaded) {h:.4f} + D {kl(loaded, fair):.4f} = cross-entropy {c:.4f} = log2 6 for any data under the fair code")

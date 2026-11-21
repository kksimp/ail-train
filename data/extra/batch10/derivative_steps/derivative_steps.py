import math

x = 1.0
exact = math.cos(x)
print(f"exact derivative of sin at 1: {exact:.12f}")
h = 0.1
prev_f = 0.0
prev_c = 0.0
for _ in range(4):
    fwd = (math.sin(x + h) - math.sin(x)) / h
    ctr = (math.sin(x + h) - math.sin(x - h)) / (2.0 * h)
    ef = abs(fwd - exact)
    ec = abs(ctr - exact)
    if prev_f > 0.0:
        print(f"h {h:.4f}: forward error {ef:.10f} (/{prev_f / ef:.0f}), central error {ec:.10f} (/{prev_c / ec:.0f})")
    else:
        print(f"h {h:.4f}: forward error {ef:.10f}, central error {ec:.10f}")
    prev_f = ef
    prev_c = ec
    h = h / 10.0
print("each tenth of h cuts the forward error 10 times and the central error 100 times")
xs = [0.0, 0.5, 1.0, 1.5, 2.0]
second = [(math.exp(v + 0.001) - 2.0 * math.exp(v) + math.exp(v - 0.001)) / 0.000001 for v in xs]
shown = ", ".join(f"{s:.4f}" for s in second)
print(f"second derivative of e^x at 0, 0.5, 1, 1.5, 2: {shown}")

def step(t, r):
    old = list(t)
    for i in range(1, len(t) - 1):
        t[i] = old[i] + r * (old[i - 1] - 2.0 * old[i] + old[i + 1])

def show(t):
    return " ".join(f"{x:.1f}" for x in t)

def run(r, steps):
    t = [100.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 0.0]
    for n in range(steps):
        step(t, r)
    return t

for steps in [0, 5, 20, 80, 300]:
    t = run(0.3, steps)
    print(f"r 0.3 after {steps:>3}: {show(t)}")
wild = run(0.6, 40)
worst = 0.0
for x in wild:
    worst = abs(x) if abs(x) > worst else worst
print(f"r 0.6 after  40: largest |T| {worst:.0f}, the scheme is unstable")

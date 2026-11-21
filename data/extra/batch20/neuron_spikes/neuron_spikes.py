import math

def step(st, cur, t, dt):
    tau = 10.0
    rest = -70.0
    resist = 10.0
    st[0] += (-(st[0] - rest) + resist * cur) / tau * dt
    if st[0] >= -50.0:
        st[1].append(t)
        st[0] = -65.0

def predicted_hz(cur):
    drive = 10.0 * cur
    if drive <= 20.0:
        return 0.0
    period = 10.0 * math.log((drive - 5.0) / (drive - 20.0))
    return 1000.0 / period

for amps in [1.5, 2.5, 3.0, 4.0, 6.0]:
    st = [-70.0, []]
    step_no = 0
    while step_no < 5000:
        step_no += 1
        step(st, amps, float(step_no) * 0.1, 0.1)
    count = len(st[1])
    first = f"first at {st[1][0]:.1f} ms" if count > 0 else "silent"
    print(f"{amps} nA: {count:>3} spikes in 500 ms ({count * 2} Hz), {first}, theory {predicted_hz(amps):.1f} Hz")

total = 10
window = 4
lost = {"2:1", "5:1", "5:2", "8:1"}
attempts = [0] * total
base = 0
sent = 0
rnd = 1
while base < total:
    expected = base
    shown = []
    top = min(base + window, total)
    for f in range(base, top):
        attempts[f] += 1
        sent += 1
        tag = f"{f}:{attempts[f]}"
        if tag in lost:
            shown.append(f"{f}x")
        elif f == expected:
            expected += 1
            shown.append(f"{f}")
        else:
            shown.append(f"{f}-")
    print(f"round {rnd}: sent {' '.join(shown)}; ack {expected}")
    base = expected
    rnd += 1
print(f"{sent} transmissions for {total} frames (x lost, - discarded out of order)")

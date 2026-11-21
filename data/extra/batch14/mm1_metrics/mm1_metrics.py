mu = 30.0
print("coffee kiosk serving 30 an hour")
print("arrivals  load   in system  in queue  minutes in system  minutes waiting  Little check")
for lam in [10.0, 15.0, 20.0, 24.0, 27.0, 29.0]:
    r = lam / mu
    l = r / (1.0 - r)
    lq = r * r / (1.0 - r)
    w = 1.0 / (mu - lam)
    wq = r / (mu - lam)
    check = lam * w
    print(f"{lam:>8.0f} {r:>5.2f} {l:>11.2f} {lq:>9.2f} {w * 60.0:>18.1f} {wq * 60.0:>16.1f} {check:>13.2f}")
r = 24.0 / 30.0
probs = []
for n in range(5):
    p = (1.0 - r) * r ** float(n)
    probs.append(f"{p:.3f}")
print(f"at 24 an hour, chance of 0..4 people present: {', '.join(probs)}")

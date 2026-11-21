import math

def cents(num, den):
    r = num / den
    return 1200.0 * math.log(r) / math.log(2.0)

names = ["C", "G", "D", "A", "E", "B", "F#", "C#", "G#", "D#", "A#", "E#"]
notes = []
num, den = 1, 1
for name in names:
    notes.append((name, num, den))
    num = num * 3
    den = den * 2
    while num >= 2 * den:
        den = den * 2
for name, nu, de in sorted(notes, key=lambda n: int(cents(n[1], n[2]) * 1000.0)):
    c = cents(nu, de)
    step = math.floor(c / 100.0 + 0.5) * 100.0
    print(f"{name:<3} {nu:>6}/{de:<6} {c:>8.2f} cents, {c - step:>6.2f} from equal")
comma = cents(531441, 524288)
print(f"twelve fifths overshoot seven octaves by {comma:.2f} cents")

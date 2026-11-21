import math

def log2(x):
    return math.log(x) / math.log(2.0)

def tidy(x):
    return 0.0 if abs(x) < 0.05 else x

names = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
far = []
for n in range(1, 17):
    f = 110.0 * n
    semis = 12.0 * log2(f / 440.0)
    m = int(math.floor(semis + 69.0 + 0.5))
    dev = tidy(100.0 * semis - 100.0 * (m - 69))
    if abs(dev) > 15.0:
        far.append(n)
    octave = m // 12 - 1
    print(f"{n:>2} {f:>7.1f} Hz  {names[m % 12]}{octave:<3} {dev:>6.1f} cents")
print(f"partials more than 15 cents off: [{', '.join(str(x) for x in far)}]")

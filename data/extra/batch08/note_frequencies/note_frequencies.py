import math
names = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
for m in [21, 48, 60, 64, 67, 69, 72, 81, 108]:
    print(f"{m:>3} {names[m % 12] + str(m // 12 - 1):<4} {440.0 * 2.0 ** ((m - 69) / 12.0):>8.2f} Hz")
c = 1200.0 * math.log(1.5) / math.log(2.0)
print(f"pure fifth {c:.2f} cents, tempered 700.00, gap {c - 700.0:.2f}")

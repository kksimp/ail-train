def key_name(k):
    names = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
    m = k + 20
    return f"{names[m % 12]}{m // 12 - 1}"

def is_black(k):
    return (k + 20) % 12 in [1, 3, 6, 8, 10]

for k in [1, 2, 40, 42, 49, 54, 88]:
    colour = "black" if is_black(k) else "white"
    print(f"key {k:>2}: {key_name(k):<4} {colour}")
white = black = 0
for k in range(1, 89):
    if is_black(k):
        black += 1
    else:
        white += 1
print(f"{white} white keys and {black} black keys")
octave_four = [key_name(k) for k in range(1, 89) if key_name(k).endswith("4") and not is_black(k)]
print(f"white keys in octave 4: {' '.join(octave_four)}")

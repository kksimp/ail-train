NAMES = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
def digit_at(s, i, words):
    ch = s[i]
    if ch.isdigit():
        return int(ch)
    if words:
        for k, w in enumerate(NAMES):
            if s[i:].startswith(w):
                return k + 1
    return None

def code(s, words):
    first = last = -1
    for i in range(len(s)):
        d = digit_at(s, i, words)
        if d is not None:
            if first < 0: first = d
            last = d
    return 0 if first < 0 else first * 10 + last

labels = ["pq3sevenfour8x", "twone4kz", "xninesix5eightwo", "7abc", "fivezero1nineteen", "3eightthree"]
p1 = p2 = 0
for l in labels:
    a = code(l, False); b = code(l, True)
    print(f"{l:<18} {a:>3} {b:>3}")
    p1 += a; p2 += b
print(f"part 1: {p1}")
print(f"part 2: {p2}")

names = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
hours = [[[540, 780], [840, 1050]], [[540, 780], [840, 1050]], [[540, 780]], [[540, 780], [840, 1170]], [[540, 1050]], [[600, 960]], []]
holidays = {7}

def hhmm(t):
    return f"{t // 60:02d}:{t % 60:02d}"

def is_open(day, t):
    if day in holidays:
        return False
    return any(w[0] <= t < w[1] for w in hours[day % 7])

def next_open(day, t):
    for d in range(day, day + 14):
        if d in holidays:
            continue
        for w in hours[d % 7]:
            if d > day or w[0] > t:
                return [d, w[0]]
    return [-1, 0]

for day, t in [(0, 600), (0, 800), (2, 900), (5, 1000), (6, 700), (3, 1100), (8, 530)]:
    when = f"{names[day % 7]} {hhmm(t)}"
    if is_open(day, t):
        print(f"{when}: open")
    else:
        n = next_open(day, t)
        later = "today" if n[0] == day else names[n[0] % 7]
        print(f"{when}: closed, opens {later} {hhmm(n[1])}")

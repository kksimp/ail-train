course = [31, 45, 38, 52, 33]
runs = [("Ada", 600, 2434, [31, 45, 38, 52, 33]), ("Bram", 720, 2430, [31, 38, 45, 52, 33]), ("Cass", 840, 2742, [31, 45, 44, 38, 52, 33]), ("Dev", 960, 2615, [31, 45, 38, 33]), ("Ezra", 1080, 2857, [31, 31, 45, 38, 52, 52, 33])]

def first_missing(course, punches):
    at = 0
    for c in course:
        found = False
        while at < len(punches):
            at += 1
            if punches[at - 1] == c:
                found = True
                break
        if not found:
            return c
    return None

def mmss(s):
    return f"{s // 60}:{s % 60:02d}"

valid = [r for r in runs if first_missing(course, r[3]) is None]
for i, r in enumerate(sorted(valid, key=lambda r: r[2] - r[1])):
    print(f"{i + 1}. {r[0]:<5} {mmss(r[2] - r[1])}")
for r in runs:
    c = first_missing(course, r[3])
    if c is not None:
        print(f"mp {r[0]:<5} missed control {c} ({mmss(r[2] - r[1])} not counted)")

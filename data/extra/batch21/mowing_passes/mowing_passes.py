lawns = [("front", 12, 650), ("back", 25, 1100), ("verge", 30, 120), ("orchard", 18, 1480)]

def passes(w):
    return (w + 39) // 40

def seconds(l):
    n = passes(l[2])
    return n * l[1] * 60 // 50 + (n - 1) * 6

def mmss(s):
    return f"{s // 60}:{s % 60:02d}"

total = 0
for l in lawns:
    n = passes(l[2])
    total += seconds(l)
    print(f"{l[0]:<8} {n:>2} passes, {n * l[1]:>3} m walked, {mmss(seconds(l))}")
print(f"whole garden: {mmss(total)}")
print(f"longest job: {max(lawns, key=seconds)[0]}")

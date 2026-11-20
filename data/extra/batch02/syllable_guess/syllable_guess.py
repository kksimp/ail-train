def syl(word):
    w = [c for c in word.lower() if c.isalpha()]
    g, prev = 0, False
    for c in w:
        v = c in "aeiouy"
        if v and not prev: g += 1
        prev = v
    if len(w) > 2 and w[-1] == "e" and w[-2] not in "aeiouy" and g > 1: g -= 1
    return max(g, 1)
for w in ["cake", "banana", "rhythm", "the", "beautiful", "queue", "make", "table"]:
    print(f"{w}: {syl(w)}")
for line in ["An old silent pond", "A frog jumps into the pond", "Splash! Silence again"]:
    print(f"{sum(syl(x) for x in line.split()):>2} {line}")

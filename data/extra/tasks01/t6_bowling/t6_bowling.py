import sys
def score(line):
    r = []
    for t in line.split():
        try:
            v = int(t)
        except ValueError:
            return "invalid"
        if v < 0 or v > 10:
            return "invalid"
        r.append(v)
    n = len(r)
    i = 0
    for f in range(9):
        if i >= n:
            return "incomplete"
        a = r[i]
        if a == 10:
            i += 1
            continue
        if i + 1 >= n:
            return "incomplete"
        if a + r[i + 1] > 10:
            return "invalid"
        i += 2
    if i >= n:
        return "incomplete"
    a = r[i]
    if a == 10:
        if i + 2 >= n:
            return "incomplete"
        b, c = r[i + 1], r[i + 2]
        if b < 10 and b + c > 10:
            return "invalid"
        end = i + 3
    else:
        if i + 1 >= n:
            return "incomplete"
        b = r[i + 1]
        if a + b > 10:
            return "invalid"
        if a + b == 10:
            if i + 2 >= n:
                return "incomplete"
            end = i + 3
        else:
            end = i + 2
    if end < n:
        return "invalid"
    total = 0
    i = 0
    for f in range(9):
        if r[i] == 10:
            total += 10 + r[i + 1] + r[i + 2]
            i += 1
        elif r[i] + r[i + 1] == 10:
            total += 10 + r[i + 2]
            i += 2
        else:
            total += r[i] + r[i + 1]
            i += 2
    total += sum(r[i:end])
    return str(total)
lines = sys.stdin.read().split("\n")
if lines and lines[-1] == "":
    lines.pop()
for l in lines:
    print(score(l.rstrip("\r")))

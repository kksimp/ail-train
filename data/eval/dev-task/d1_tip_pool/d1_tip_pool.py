import sys

lines = [l for l in sys.stdin.read().splitlines() if l.strip() != ""]
total = 0
if lines:
    t = lines[0].strip()
    body = t[1:] if t.startswith("-") else t
    if body.isascii() and body.isdigit():
        total = int(t)
names = []
hours = []
for l in lines[1:]:
    w = l.split()
    if len(w) != 2:
        continue
    s = w[1]
    body = s[1:] if s.startswith("-") else s
    if not (body.isascii() and body.isdigit()):
        continue
    h = int(s)
    if h < 0:
        continue
    names.append(w[0])
    hours.append(h)
sum_h = sum(hours)
if sum_h == 0:
    print("no hours")
else:
    shares = [total * h // sum_h for h in hours]
    left = total - sum(shares)
    for i in range(len(shares)):
        if left > 0 and hours[i] > 0:
            shares[i] += 1
            left -= 1
    for n, s in zip(names, shares):
        print(f"{n}: {s}")

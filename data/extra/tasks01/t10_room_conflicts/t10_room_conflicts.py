import sys


def parse(line):
    f = line.split(" ")
    if len(f) != 4:
        return None
    try:
        s = int(f[1])
        e = int(f[2])
    except ValueError:
        return None
    if not (f[1].lstrip("-").isdigit() and f[2].lstrip("-").isdigit()):
        return None
    if s < 0 or s >= e:
        return None
    return (f[0], s, e, f[3])


accepted = []
rejected = bad = 0
for n, line in enumerate(sys.stdin.read().splitlines(), 1):
    if line.strip() == "":
        continue
    b = parse(line)
    if b is None:
        print(f"BAD line {n}")
        bad += 1
        continue
    room, s, e, name = b
    c = None
    for x in accepted:
        if x[0] == room and x[1] < e and s < x[2]:
            c = x[3]
            break
    if c is not None:
        print(f"REJECT {name} {room} {s}-{e} conflicts with {c}")
        rejected += 1
    else:
        print(f"OK {name} {room} {s}-{e}")
        accepted.append(b)
print(f"accepted {len(accepted)} rejected {rejected} bad {bad}")

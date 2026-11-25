import sys


def parse(p):
    items = []  # [set-of-codes-or-None(any), negate, quant]
    i = 0
    while i < len(p):
        c = p[i]
        i += 1
        if c in "*?":
            if not items or items[-1][2] != "":
                return None
            items[-1][2] = c
        elif c == "[":
            neg = False
            if i < len(p) and p[i] == "^":
                neg = True
                i += 1
            j = p.find("]", i)
            if j < 0:
                return None
            body = p[i:j]
            i = j + 1
            if not body:
                return None
            chars = set()
            k = 0
            while k < len(body):
                if k + 2 < len(body) and body[k + 1] == "-":
                    lo, hi = ord(body[k]), ord(body[k + 2])
                    if hi < lo:
                        return None
                    chars.update(range(lo, hi + 1))
                    k += 3
                else:
                    chars.add(ord(body[k]))
                    k += 1
            items.append([chars, neg, ""])
        elif c == ".":
            items.append([set(), True, ""])
        else:
            items.append([{ord(c)}, False, ""])
    return items


def hit(item, ch):
    return (ord(ch) in item[0]) != item[1]


def match(items, i, t, j):
    if i == len(items):
        return j == len(t)
    item = items[i]
    ok = j < len(t) and hit(item, t[j])
    q = item[2]
    if q == "*":
        return match(items, i + 1, t, j) or (ok and match(items, i, t, j + 1))
    if q == "?":
        return match(items, i + 1, t, j) or (ok and match(items, i + 1, t, j + 1))
    return ok and match(items, i + 1, t, j + 1)


for n, line in enumerate(sys.stdin.read().splitlines(), 1):
    if " " not in line:
        print("%d: bad line" % n)
        continue
    pat, text = line.split(" ", 1)
    items = parse(pat)
    if items is None:
        print("%d: bad pattern" % n)
    else:
        print("%d: %s" % (n, "match" if match(items, 0, text, 0) else "no match"))

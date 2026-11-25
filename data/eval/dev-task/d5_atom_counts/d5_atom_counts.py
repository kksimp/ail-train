import re
import sys


def parse(f):
    pos = 0

    def number():
        nonlocal pos
        m = re.compile(r"[0-9]+").match(f, pos)
        if not m:
            return 1
        pos = m.end()
        v = int(m.group())
        if v == 0 or len(m.group()) > 3:
            raise ValueError
        return v

    def group(top):
        nonlocal pos
        res = {}
        while pos < len(f):
            c = f[pos]
            if c == ")":
                if top:
                    raise ValueError
                return res
            if c == "(":
                pos += 1
                inner = group(False)
                if pos >= len(f) or f[pos] != ")":
                    raise ValueError
                pos += 1
                if not inner:
                    raise ValueError
                m = number()
                for k, v in inner.items():
                    res[k] = res.get(k, 0) + v * m
            elif "A" <= c <= "Z":
                sym = c
                pos += 1
                if pos < len(f) and "a" <= f[pos] <= "z":
                    sym += f[pos]
                    pos += 1
                res[sym] = res.get(sym, 0) + number()
            else:
                raise ValueError
        return res

    r = group(True)
    if not r:
        raise ValueError
    return r


for line in sys.stdin.read().splitlines():
    f = line.strip()
    if not f:
        continue
    try:
        c = parse(f)
    except ValueError:
        print(f"{f}: invalid")
        continue
    print(f"{f}: " + " ".join(f"{k}={c[k]}" for k in sorted(c)) + f" total={sum(c.values())}")

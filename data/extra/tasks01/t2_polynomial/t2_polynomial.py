import re, sys

def ok_int(t):
    return re.fullmatch(r"-?[0-9]{1,3}", t) is not None and -100 <= int(t) <= 100

def render(cs):
    # cs: highest degree first
    deg = len(cs) - 1
    out = ""
    for i, c in enumerate(cs):
        e = deg - i
        if c == 0:
            continue
        a = abs(c)
        body = ""
        if e == 0:
            body = str(a)
        else:
            body = ("" if a == 1 else str(a)) + ("x" if e == 1 else f"x^{e}")
        if out == "":
            out = ("-" if c < 0 else "") + body
        else:
            out += (" - " if c < 0 else " + ") + body
    return out or "0"

def deriv(cs):
    deg = len(cs) - 1
    return [c * (deg - i) for i, c in enumerate(cs[:-1])] or [0]

def ev(cs, x):
    v = 0
    for c in cs:
        v = v * x + c
    return v

def main():
    lines = sys.stdin.read().split("\n")
    if lines[-1] == "":
        lines.pop()
    toks = lines[0].split() if lines else []
    if not toks or len(toks) > 7 or not all(ok_int(t) for t in toks):
        print("error: bad coefficients")
        return
    cs = [int(t) for t in toks]
    ds = deriv(cs)
    print(f"p(x) = {render(cs)}")
    print(f"p'(x) = {render(ds)}")
    for k, raw in enumerate(lines[1:], 2):
        t = raw.strip()
        if t == "":
            continue
        if not ok_int(t):
            print(f"line {k}: bad point")
            continue
        x = int(t)
        print(f"x={x} p={ev(cs, x)} dp={ev(ds, x)}")

main()

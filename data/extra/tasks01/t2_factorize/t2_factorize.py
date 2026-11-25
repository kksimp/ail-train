import sys

def factor(n):
    out = []
    p = 2
    while p * p <= n:
        if n % p == 0:
            e = 0
            while n % p == 0:
                n //= p
                e += 1
            out.append((p, e))
        p += 1 if p == 2 else 2
    if n > 1:
        out.append((n, 1))
    return out

def main():
    lines = sys.stdin.read().split("\n")
    if lines[-1] == "":
        lines.pop()
    done = 0
    for k, raw in enumerate(lines, 1):
        t = raw.strip()
        if t == "":
            continue
        if not (t.isascii() and t.isdigit()):
            print(f"line {k}: invalid")
            continue
        n = int(t)
        if n < 2 or n > 10**12:
            print(f"line {k}: out of range")
            continue
        f = factor(n)
        if len(f) == 1 and f[0][1] == 1:
            print(f"{n} = {n} (prime)")
        else:
            print(f"{n} = " + " * ".join(f"{p}^{e}" if e > 1 else f"{p}" for p, e in f))
        done += 1
    print(f"factored {done}")

main()

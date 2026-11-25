import sys

def add(a, b):
    a = a.lstrip("0") or "0"
    b = b.lstrip("0") or "0"
    n = max(len(a), len(b))
    a, b = a.rjust(n, "0"), b.rjust(n, "0")
    out = []
    carry = 0
    for i in range(n - 1, -1, -1):
        s = int(a[i]) + int(b[i]) + carry
        out.append(str(s % 10))
        carry = s // 10
    if carry:
        out.append(str(carry))
    return "".join(reversed(out))

def digits(t):
    return t != "" and all(c in "0123456789" for c in t)

def main():
    lines = sys.stdin.read().split("\n")
    if lines[-1] == "":
        lines.pop()
    total = "0"
    for k, raw in enumerate(lines, 1):
        f = raw.split()
        if not f:
            continue
        if len(f) != 2 or not digits(f[0]) or not digits(f[1]):
            print(f"line {k}: invalid")
            continue
        s = add(f[0], f[1])
        print(s)
        total = add(total, s)
    print(f"sum of sums: {total}")

main()

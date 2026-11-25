import sys

DIGITS = "0123456789abcdefghijklmnopqrstuvwxyz"

def is_dec(t):
    return t.isascii() and t.isdigit()

def main():
    lines = sys.stdin.read().split("\n")
    if lines[-1] == "":
        lines.pop()
    ok = err = 0
    for k, raw in enumerate(lines, 1):
        f = raw.split()
        if not f:
            continue
        if len(f) != 3 or not is_dec(f[0]) or not is_dec(f[1]):
            print(f"line {k}: bad format")
            err += 1
            continue
        a, b = int(f[0]), int(f[1])
        if not (2 <= a <= 36 and 2 <= b <= 36):
            print(f"line {k}: bad base")
            err += 1
            continue
        v = 0
        bad = None
        for c in f[2].lower():
            d = DIGITS.find(c)
            if d < 0 or d >= a:
                bad = c
                break
            v = v * a + d
        if bad is not None:
            print(f"line {k}: bad digit {bad}")
            err += 1
            continue
        out = ""
        while v > 0:
            out = DIGITS[v % b] + out
            v //= b
        print(out or "0")
        ok += 1
    print(f"ok {ok} errors {err}")

main()

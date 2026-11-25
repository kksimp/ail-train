import sys
from functools import lru_cache

def main():
    lines = sys.stdin.read().split("\n")
    if lines and lines[-1] == "":
        lines.pop()
    lines = [l[:-1] if l.endswith("\r") else l for l in lines]
    if not lines:
        print("no pattern")
        return
    p = lines[0]
    for i, c in enumerate(p):
        if c == "*" and (i == 0 or p[i - 1] == "*"):
            print("invalid pattern")
            return

    def match(t):
        @lru_cache(maxsize=None)
        def m(i, j):
            if i == len(p):
                return j == len(t)
            first = j < len(t) and (p[i] == "." or p[i] == t[j])
            if i + 1 < len(p) and p[i + 1] == "*":
                return m(i + 2, j) or (first and m(i, j + 1))
            return first and m(i + 1, j + 1)
        return m(0, 0)

    for t in lines[1:]:
        print('"%s": %s' % (t, "yes" if match(t) else "no"))

main()

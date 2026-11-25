## comm of two sorted blocks
import sys

lines = sys.stdin.read().split("\n")
if lines and lines[-1] == "":
    lines.pop()
if lines:
    opt = lines[0]
    data = lines[1:]
    if "---" in data:
        k = data.index("---")
        a, b = data[:k], data[k + 1:]
    else:
        a, b = data, []
    show = [str(c) not in opt for c in (1, 2, 3)]

    def out(col, text):
        if not show[col - 1]:
            return
        print("\t" * sum(show[:col - 1]) + text)

    while a or b:
        if not b or (a and a[0] < b[0]):
            out(1, a.pop(0))
        elif not a or b[0] < a[0]:
            out(2, b.pop(0))
        else:
            out(3, a.pop(0))
            b.pop(0)

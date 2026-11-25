import sys, re

def main():
    lines = sys.stdin.read().split("\n")
    if lines and lines[-1] == "":
        lines.pop()
    lines = [l[:-1] if l.endswith("\r") else l for l in lines]
    if len(lines) < 2:
        print("bad input")
        return
    w = lines[0].split(" ")
    row = lines[1]
    if len(w) != 2 or not re.fullmatch(r"[0-9]+", w[0]) or not re.fullmatch(r"[0-9]+", w[1]):
        print("bad input")
        return
    rule, steps = int(w[0]), int(w[1])
    if rule > 255 or steps > 30 or not re.fullmatch(r"[01]{1,40}", row):
        print("bad input")
        return
    cells = [int(c) for c in row]
    n = len(cells)
    print("".join("#" if c else "." for c in cells))
    for _ in range(steps):
        cells = [(rule >> (4 * cells[(i - 1) % n] + 2 * cells[i] + cells[(i + 1) % n])) & 1 for i in range(n)]
        print("".join("#" if c else "." for c in cells))

main()

import sys

def main():
    lines = sys.stdin.read().splitlines()
    if not lines:
        print("no input")
        return
    t = lines[0].strip()
    if not t.isdigit() or not (1 <= int(t) <= 8):
        print("bad width")
        return
    w = int(t)
    changed = 0
    for ln in lines[1:]:
        out = []
        col = 0
        had = False
        for ch in ln:
            if ch == "\t":
                had = True
                pad = w - col % w
                out.append(" " * pad)
                col += pad
            else:
                out.append(ch)
                col += 1
        if had:
            changed += 1
        print("".join(out))
    print(f"changed={changed}")

main()

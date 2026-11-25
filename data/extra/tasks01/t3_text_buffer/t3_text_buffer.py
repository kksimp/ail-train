import sys


def main():
    lines = sys.stdin.read().split("\n")
    if lines[-1] == "":
        lines.pop()
    buf = ""
    undo, redo = [], []
    for line in lines:
        if line.strip() == "":
            continue
        p = line.split(" ", 1)
        c = p[0]
        if c == "append" and len(p) == 2 and p[1] != "":
            undo.append(buf)
            redo = []
            buf += p[1]
        elif c == "delete" and len(p) == 2 and p[1].isascii() and p[1].isdigit() and int(p[1]) >= 1:
            undo.append(buf)
            redo = []
            n = int(p[1])
            buf = "" if n >= len(buf) else buf[: len(buf) - n]
        elif c == "undo" and len(p) == 1:
            if undo:
                redo.append(buf)
                buf = undo.pop()
            else:
                print("error: nothing to undo")
        elif c == "redo" and len(p) == 1:
            if redo:
                undo.append(buf)
                buf = redo.pop()
            else:
                print("error: nothing to redo")
        elif c == "show" and len(p) == 1:
            print(f"[{buf}]")
        else:
            print("error: bad command")
    print(f"edits: {len(undo)}")


main()

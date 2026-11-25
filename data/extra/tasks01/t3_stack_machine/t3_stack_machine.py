import sys


def trunc_div(a, b):
    q = abs(a) // abs(b)
    return q if (a < 0) == (b < 0) else -q


def main():
    text = sys.stdin.read()
    lines = text.split("\n")
    if lines and lines[-1] == "":
        lines.pop()
    st = []
    for k, line in enumerate(lines, 1):
        w = line.split()
        if not w:
            continue
        c = w[0]
        err = None
        if c == "push" and len(w) == 2:
            try:
                st.append(int(w[1]) if w[1].lstrip("-").isdigit() and w[1] != "-" else None)
                if st[-1] is None:
                    st.pop()
                    err = "bad number"
            except ValueError:
                err = "bad number"
        elif c == "push":
            err = "bad number" if len(w) == 1 else "unknown command"
        elif len(w) != 1:
            err = "unknown command"
        elif c == "pop":
            if st:
                st.pop()
            else:
                err = "underflow"
        elif c == "dup":
            if st:
                st.append(st[-1])
            else:
                err = "underflow"
        elif c == "swap":
            if len(st) >= 2:
                st[-1], st[-2] = st[-2], st[-1]
            else:
                err = "underflow"
        elif c in ("add", "sub", "mul", "div"):
            if len(st) < 2:
                err = "underflow"
            elif c == "div" and st[-1] == 0:
                err = "division by zero"
            else:
                b = st.pop()
                a = st.pop()
                st.append(a + b if c == "add" else a - b if c == "sub" else a * b if c == "mul" else trunc_div(a, b))
        elif c == "print":
            if st:
                print(st[-1])
            else:
                err = "underflow"
        else:
            err = "unknown command"
        if err:
            print(f"line {k}: {err}")
    print("stack:" + "".join(" " + str(v) for v in st))


main()

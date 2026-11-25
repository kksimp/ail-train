import sys, re

def tdiv(a, b):
    q = abs(a) // abs(b)
    return q if (a < 0) == (b < 0) else -q

def ev(line, vars):
    st = []
    for tok in line.split():
        if re.fullmatch(r"-?[0-9]+", tok):
            st.append(int(tok))
        elif tok in ("+", "-", "*", "/", "%"):
            if len(st) < 2:
                return "error: stack underflow"
            b = st.pop()
            a = st.pop()
            if tok == "+":
                st.append(a + b)
            elif tok == "-":
                st.append(a - b)
            elif tok == "*":
                st.append(a * b)
            else:
                if b == 0:
                    return "error: division by zero"
                q = tdiv(a, b)
                st.append(q if tok == "/" else a - q * b)
        elif re.fullmatch(r"[a-z]+", tok):
            if tok not in vars:
                return "error: unknown variable " + tok
            st.append(vars[tok])
        elif re.fullmatch(r"=[a-z]+", tok):
            if not st:
                return "error: stack underflow"
            vars[tok[1:]] = st.pop()
        else:
            return "error: bad token " + tok
    return " ".join(map(str, st)) if st else "(empty)"

vars = {}
for line in sys.stdin.read().splitlines():
    if line.strip() == "":
        continue
    print(ev(line, vars))

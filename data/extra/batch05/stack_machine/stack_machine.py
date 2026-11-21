def run(p):
    st = []; o = []
    for t in p.split(" "):
        try: st.append(int(t)); continue
        except ValueError: pass
        if t == "print":
            if not st: return None, "print on empty stack"
            o.append(str(st[-1])); continue
        if t == "dup":
            if not st: return None, "dup on empty stack"
            st.append(st[-1]); continue
        if len(st) < 2: return None, f"{t} needs two values"
        b = st.pop(); a = st.pop()
        if t == "add": st.append(a + b)
        elif t == "mul": st.append(a * b)
        elif t == "sub": st.append(a - b)
        elif t == "swap": st += [b, a]
        else: return None, f"unknown word {t}"
    return " ".join(o), None
for p in ["2 3 add print", "4 dup mul print 1 sub print", "1 2 swap sub print", "5 add", "3 4 pow"]:
    r, e = run(p); print(f"{p} => {r}" if e is None else f"{p} => error: {e}")

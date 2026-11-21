def scan(t):
    st = []; d = 0
    for i, c in enumerate(t):
        if c in "([{":
            st.append({"(": ")", "[": "]", "{": "}"}[c]); d = max(d, len(st))
        elif c in ")]}":
            if not st: return f"unexpected {c} at {i}"
            w = st.pop()
            if w != c: return f"expected {w} at {i}, found {c}"
    if st: return f"{len(st)} left open"
    return f"ok, depth {d}"
for t in ["(a[b]{c})", "f(x)", "((([])))", "(a]", "a)b", "[(", "", "{[()()]}[]"]:
    print(f"{t:<12} {scan(t)}")

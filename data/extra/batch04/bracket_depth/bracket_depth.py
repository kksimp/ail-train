def ck(s):
    st = []; d = 0; cl = {"(": ")", "[": "]", "{": "}"}
    for i, c in enumerate(s):
        if c in cl:
            st.append(cl[c]); d = max(d, len(st))
        elif c in ")]}":
            if not st: return f"unexpected {c} at {i}"
            w = st.pop()
            if w != c: return f"expected {w} at {i}, found {c}"
    if st: return f"{len(st)} left open"
    return f"balanced, depth {d}"
for s in ["(a[b]{c})", "((()))", "([)]", "{[}", "a)b", "[[{}]", "x"]: print(f"{s}: {ck(s)}")

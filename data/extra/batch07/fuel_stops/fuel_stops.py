def pl(S, f, r):
    st = []; tf = 0; P = S + [f]
    for i, p in enumerate(P):
        if p - tf > r:
            if i == 0: return None
            la = P[i - 1]
            if p - la > r or la == tf: return None
            st.append(la); tf = la
    return st
for S, f in [([120, 290, 410, 560, 700, 880], 1000), ([150, 380, 790], 1100), ([90, 200, 330], 380), ([300, 450], 1000)]:
    s = pl(S, f, 400)
    if s is None: print(f"{f} km: can't be done")
    elif not s: print(f"{f} km: no stops needed")
    else: print(f"{f} km: {len(s)} stop(s) at {', '.join(map(str, s))}")

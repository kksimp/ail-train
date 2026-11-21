f = {"KX12 ABC": 100, "LM65 DEF": 130, "PQ19 GHI": 145, "RS70 JKL": 160, "TU22 MNO": 175}
s = {"KX12 ABC": 208, "LM65 DEF": 226, "PQ19 GHI": 280, "TU22 MNO": 250}
for p in sorted(f):
    if p not in s: print(f"{p}: did not reach the second camera"); continue
    sec = s[p] - f[p]; k = 2400 * 36 // (sec * 10)
    v = "ok" if k <= 80 else "warning" if k <= 90 else "fine"
    print(f"{p}: {sec}s, {k} km/h, {v}")

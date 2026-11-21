B = [["A", "B", "C"], ["B", "A", "C"], ["C", "B", "A"], ["A", "C", "B"], ["B", "C", "A"], ["C", "A", "B"], ["B", "A", "C"], ["A", "B", "C"], ["B", "C", "A"]]
al = ["A", "B", "C"]; rd = 1
while True:
    t = {c: 0 for c in al}
    for b in B:
        tp = [c for c in b if c in al]
        if tp: t[tp[0]] += 1
    print(f"round {rd}: " + " ".join(f"{c}={t[c]}" for c in al))
    ld = max(al, key=lambda c: t[c])
    if t[ld] * 2 > len(B): print(f"winner: {ld}"); break
    lo = min(al, key=lambda c: (t[c], c)); print(f"  {lo} is out")
    al = [c for c in al if c != lo]; rd += 1

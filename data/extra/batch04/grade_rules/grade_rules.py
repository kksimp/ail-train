M = [91, 78, 65, 59, 84, 40, 72]
S = [(90, "A"), (80, "B"), (70, "C"), (60, "D")]; G = [(85, "A"), (75, "B"), (65, "C"), (50, "D")]
def le(m, b):
    for x in b:
        if m >= x[0]: return x[1]
    return "F"
gr = lambda c, b: [le(min(c(m), 100), b) for m in M]
print(f"strict, no curve: {' '.join(gr(lambda m: m, S))}")
print(f"strict, +5 curve: {' '.join(gr(lambda m: m + 5, S))}")
print(f"gentle, no curve: {' '.join(gr(lambda m: m, G))}")
print(f"gentle with curve passes {sum(1 for g in gr(lambda m: m + 5, G) if g != 'F')} of {len(M)}")

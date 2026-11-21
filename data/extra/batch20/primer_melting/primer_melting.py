def gc_count(s):
    return sum(1 for c in s if c == "G" or c == "C")

def tm(s):
    n = len(s)
    gc = gc_count(s)
    if n < 14:
        return float(2 * (n - gc) + 4 * gc)
    return 64.9 + 41.0 * (float(gc) - 16.4) / float(n)

def problems(s):
    out = []
    share = float(gc_count(s)) / float(len(s)) * 100.0
    if share < 40.0 or share > 60.0:
        out.append(f"GC {share:.0f}%")
    last = s[-1]
    if last != "G" and last != "C":
        out.append("no 3' clamp")
    if "AAAA" in s or "TTTT" in s or "GGGG" in s or "CCCC" in s:
        out.append("run of 4")
    return out

for fwd, rev in [("AGCTTGCATGCCTGCAGG", "GACGGCCAGTGAATTCGA"), ("ATTTTAGCATCG", "GCGCGGCCGC"), ("TGACCTGAAGCTTGAGTC", "CAGTTTCGAGCAAAATTA")]:
    a = tm(fwd)
    b = tm(rev)
    for s in [fwd, rev]:
        issues = problems(s)
        note = "ok" if not issues else ", ".join(issues)
        print(f"{s:<20} {len(s)} nt, Tm {tm(s):.1f} C, {note}")
    gap = abs(a - b)
    verdict = "matched" if gap <= 5.0 else "mismatched"
    print(f"  pair Tm gap {gap:.1f} C: {verdict}")

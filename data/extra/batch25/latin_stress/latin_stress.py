def heavy(s):
    last = s[-1]
    long_vowel = any(c in "āēīōū" for c in s)
    closed = last not in "aeiouāēīōū"
    return long_vowel or closed or "ae" in s or "au" in s or "oe" in s

def stress_index(sylls):
    n = len(sylls)
    if n < 3:
        return 0
    return n - 2 if heavy(sylls[n - 2]) else n - 3

words = ["a.mī.cus", "do.mi.nus", "ma.gis.ter", "fe.nes.tra", "in.su.la", "ro.sa", "pa.tri.a", "ar.bo.rem", "a.gri.co.la", "for.tū.na", "cae.lum", "Ro.mā.nus"]
penult = 0
for w in words:
    sylls = w.split(".")
    weights = "".join("H" if heavy(s) else "L" for s in sylls)
    at = stress_index(sylls)
    if at == len(sylls) - 2:
        penult += 1
    shown = []
    for i, s in enumerate(sylls):
        shown.append("'" + s if i == at else s)
    marked = "".join(shown)
    print(f"{w:<11} {weights:<4} {marked}")
print(f"penult stressed in {penult} of {len(words)}")

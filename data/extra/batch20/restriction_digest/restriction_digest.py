def cuts(dna, site, cut_at):
    out = []
    frm = 0
    while frm + len(site) <= len(dna):
        at = dna[frm:].find(site)
        if at < 0:
            break
        out.append(frm + at + cut_at)
        frm = frm + at + 1
    return out

def fragments(total, positions):
    edges = [0] + sorted(positions) + [total]
    out = [edges[i + 1] - edges[i] for i in range(len(edges) - 1)]
    return sorted(out)[::-1]

pieces = ["ATCGGAATTCTTAGC", "CGGATCCAAGTTACG", "GCAAGCTTGGCATTA", "CCGAATTCGGTACCA", "TGGTTAGCAAGCTTCA", "GGCTAGGATCCTTAC", "GTTACCATGCA"]
dna = "".join(pieces)
enzymes = [("EcoRI", "GAATTC", 1), ("BamHI", "GGATCC", 1), ("HindIII", "AAGCTT", 1)]
print(f"{len(dna)} bp linear DNA")
every = []
for name, site, cut_at in enzymes:
    c = cuts(dna, site, cut_at)
    every.extend(c)
    print(f"{name:<7} {site}: cuts at {c}, fragments {fragments(len(dna), c)}")
print(f"all three together: {fragments(len(dna), every)}")

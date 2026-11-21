import math

def p_distance(a, b):
    diff = sum(1 for x, y in zip(a, b) if x != y)
    return float(diff) / float(len(a))

def jc(p):
    if p >= 0.75:
        return None
    return -0.75 * math.log(1.0 - 4.0 * p / 3.0)

seqs = [("frog", "ATGGCTAGCTTACGGATCCAGTTAGCATGC"), ("toad", "ATGGCTAGTTTACGGATCCGGTTAGCATGC"), ("newt", "ATGACTGGCTTGCGAATCCAGTTGGCTTAC"), ("fish", "TTGACCGGATTGCTAACGCAGTCGGATTAA")]
for i in range(len(seqs)):
    for j in range(i + 1, len(seqs)):
        na, sa = seqs[i]
        nb, sb = seqs[j]
        p = p_distance(sa, sb)
        d = jc(p)
        shown = f"{d:.4f}" if d is not None else "saturated"
        print(f"{na}-{nb}: p {p:.4f}, Jukes-Cantor {shown}")
for p in [0.1, 0.3, 0.5, 0.7, 0.75]:
    d = jc(p)
    text = f"{d:.3f}" if d is not None else "infinite"
    print(f"p {p}: d {text}")

d = "ATGGCCATTGTAATGGGCCGCTGAAAGGGTGCCCGATAG"; gc = sum(1 for c in d if c in "GC")
print(f"length {len(d)}, GC {gc * 100 / len(d):.1f}%")
C = {"A": "T", "T": "A", "G": "C", "C": "G"}; print("reverse complement: " + "".join(C[c] for c in reversed(d)))
T = {"ATG": "M", "GCC": "A", "ATT": "I", "GTA": "V", "GGC": "G", "CGC": "R", "TGA": "*", "AAG": "K", "GGT": "G", "TAG": "*"}; p = ""; i = 0
while i + 3 <= len(d):
    a = T.get(d[i:i + 3], "?")
    if a == "*": break
    p += a; i += 3
print(f"protein: {p} ({len(p)} residues)")

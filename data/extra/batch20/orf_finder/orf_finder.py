def complement(s):
    m = {"A": "T", "T": "A", "G": "C", "C": "G"}
    return "".join(m.get(c, "G") for c in reversed(s))

def is_stop(c):
    return c == "TAA" or c == "TAG" or c == "TGA"

def orfs(s, min_codons):
    found = []
    for frame in range(3):
        i = frame
        while i + 3 <= len(s):
            if s[i:i + 3] == "ATG":
                j = i
                while j + 3 <= len(s) and not is_stop(s[j:j + 3]):
                    j += 3
                if j + 3 <= len(s) and (j - i) // 3 >= min_codons:
                    found.append([frame, i, j + 3, (j - i) // 3])
                i = j
            i += 3
    return found

dna = "CCATGGCTTCAGGTAAGCATGAAACCCTGGTTTAGCTAATGCCCATTAGGTCATTTACCATGGGTAAACCCGGGCATTGA"
print(f"{len(dna)} bases")
for strand in ["+", "-"]:
    s = dna if strand == "+" else complement(dna)
    for o in orfs(s, 5):
        print(f"strand {strand} frame {o[0] + 1}: bases {o[1] + 1}-{o[2]}, {o[3]} codons, starts {s[o[1]:o[1] + 12]}")

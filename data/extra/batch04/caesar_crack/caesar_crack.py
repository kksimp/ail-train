def sh(s, k): return "".join(chr((ord(c) - 97 + k) % 26 + 97) if c.islower() else c for c in s)
p = "the quick brown fox jumps over the lazy dog near the riverbank"; s = sh(p, 11); print(f"cipher: {s}")
b = 0; bs = -1
for k in range(26):
    sc = sum(1 for c in sh(s, k) if c in "etaoinshr")
    if sc > bs: bs = sc; b = k
print(f"key: {(26 - b) % 26}"); print(f"plain: {sh(s, b)}")

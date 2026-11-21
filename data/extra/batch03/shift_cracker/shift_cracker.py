def sh(t, k): return "".join(chr((ord(c) - 97 + k) % 26 + 97) if c.islower() else c for c in t)
sc = lambda t: sum(1 for c in t if c in "etaoinshr")
s = sh("meet me by the old oak tree at seven", 11)
print(f"cipher: {s}")
bk, bs = 0, -1
for k in range(26):
    if sc(sh(s, k)) > bs: bs = sc(sh(s, k)); bk = k
print(f"best shift back: {bk} (score {bs})")
print(f"plain: {sh(s, bk)}")

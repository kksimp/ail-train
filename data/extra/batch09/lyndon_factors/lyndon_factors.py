def factors(s):
    n = len(s)
    out = []
    i = 0
    while i < n:
        j = i + 1
        k = i
        while j < n and ord(s[k]) <= ord(s[j]):
            if ord(s[k]) < ord(s[j]):
                k = i
            else:
                k += 1
            j += 1
        while i <= k:
            out.append(s[i:i + j - k])
            i += j - k
    return out

for w in ["banana", "abracadabra", "aabab", "zebra", "abcabcab", "mississippi"]:
    fs = factors(w)
    shown = " | ".join(fs)
    kind = "Lyndon word" if len(fs) == 1 else f"{len(fs)} factors"
    print(f"{w:<12} {shown}  ({kind})")
ordered = True
parts = factors("cbacbacba")
for i in range(1, len(parts)):
    if parts[i] > parts[i - 1]:
        ordered = False
print(f"cbacbacba factors never increase: {'true' if ordered else 'false'}")

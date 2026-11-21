def counts_of(cs):
    out = [0] * 26
    for c in cs:
        out[ord(c) - 97] += 1
    return out

def windows_of(t, pat):
    m = len(pat)
    want = counts_of(pat)
    have = counts_of(t[0:m])
    hits = []
    if have == want:
        hits.append(0)
    for i in range(m, len(t)):
        have[ord(t[i]) - 97] += 1
        have[ord(t[i - m]) - 97] -= 1
        if have == want:
            hits.append(i - m + 1)
    return hits

text = "cbaebabacdtablebleatbatabcab"
for pat in ["abc", "able", "tab", "zzz"]:
    hits = windows_of(text, pat)
    parts = [f"{h}:{text[h:h + len(pat)]}" for h in hits]
    shown = "none" if not parts else " ".join(parts)
    print(f"{pat:<5} {len(hits)} windows: {shown}")

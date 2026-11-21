def encode(cs, window, ahead):
    n = len(cs)
    out = []
    i = 0
    while i < n:
        best_len = 0
        best_off = 0
        lo = max(i - window, 0)
        j = i - 1
        while j >= lo:
            k = 0
            while k < ahead and i + k < n - 1 and cs[j + k] == cs[i + k]:
                k += 1
            if k > best_len:
                best_len = k
                best_off = i - j
            j -= 1
        out.append((best_off, best_len, cs[i + best_len]))
        i += best_len + 1
    return out

def decode(ts):
    out = []
    for back, size, ch in ts:
        for k in range(size):
            out.append(out[len(out) - back])
        out.append(ch)
    return "".join(out)

for s in ["abracadabra", "aaaaaaaaaaaa", "banana_bandana", "abcabcabcabcx"]:
    ts = encode(s, 12, 6)
    shown = " ".join(f"({b},{n},{c})" for b, n, c in ts)
    ok = "ok" if decode(ts) == s else "BAD"
    print(f"{s}: {len(ts)} triples for {len(s)} letters, round trip {ok}")
    print(f"  {shown}")

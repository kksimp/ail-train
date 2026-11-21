MOD = 1000003
BASE = 257
WIN = 6

def chunks(text):
    top = 1
    for _ in range(WIN - 1):
        top = top * BASE % MOD
    out = []
    start = 0
    h = 0
    for i in range(len(text)):
        if i >= WIN:
            h = (h - ord(text[i - WIN]) * top % MOD + MOD) % MOD
        h = (h * BASE + ord(text[i])) % MOD
        size = i - start + 1
        if (size >= 4 and h % 13 == 0) or size >= 40:
            out.append(text[start:i + 1])
            start = i + 1
    if start < len(text):
        out.append(text[start:])
    return out

def fixed(text, size):
    return [text[i:min(i + size, len(text))] for i in range(0, len(text), size)]

def shared(a, b):
    have = set(a)
    return sum(1 for x in b if x in have)

before = "the archive keeps every version of every file, and a backup only sends the pieces that changed since the last run, so small edits stay cheap to store and to send"
after = "the archive keeps every single version of every file, and a backup only sends the pieces that changed since the last run, so small edits stay cheap to store and to send"
ca = chunks(before)
cb = chunks(after)
print(f"content-defined: {len(ca)} chunks before, {len(cb)} after, {shared(ca, cb)} reused")
fa = fixed(before, 16)
fb = fixed(after, 16)
print(f"fixed 16-char:   {len(fa)} chunks before, {len(fb)} after, {shared(fa, fb)} reused")
for i in range(4):
    print(f"  chunk {i}: [{cb[i]}]")

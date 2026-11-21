def fnv(word):
    h = 2166136261
    for c in word:
        h = ((h ^ ord(c)) * 16777619) % 4294967296
    return h

def simhash(text):
    votes = [0] * 32
    for w in text.split():
        h = fnv(w)
        for b in range(32):
            if ((h >> b) & 1) == 1:
                votes[b] += 1
            else:
                votes[b] -= 1
    fp = 0
    for b in range(32):
        if votes[b] > 0:
            fp = fp | (1 << b)
    return fp

def distance(a, b):
    return bin(a ^ b).count("1")

docs = ["the quick brown fox jumps over the lazy dog near the river bank", "the quick brown fox jumped over the lazy dog near the river bank", "a quick brown fox jumps over a lazy dog by the river bank", "share markets fell sharply today as investors sold technology shares", "investors sold technology shares today as markets fell sharply"]
fps = [simhash(d) for d in docs]
for i in range(len(docs)):
    print(f"doc {i}: {fps[i]:08x}")
for i in range(len(docs)):
    row = "".join(f"{distance(fps[i], fps[j]):>3}" for j in range(len(docs)))
    print(f"bits apart from doc {i}:{row}")

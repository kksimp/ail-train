def score(server, key):
    h = 2166136261
    for c in server:
        h = ((h ^ ord(c)) * 16777619) % 4294967296
    h = ((h ^ key) * 16777619) % 4294967296
    h = (h >> 15) ^ h
    h = h * 73244475 % 4294967296
    return (h >> 16) ^ h

def owner(servers, key):
    best = ""
    top = -1
    for s in servers:
        v = score(s, key)
        if v > top:
            top = v
            best = s
    return best

def loads(servers, owners):
    return " ".join(f"{s}:{owners.count(s)}" for s in servers)

servers = ["alpha", "bravo", "charlie", "delta", "echo"]
keys = [k * 37 + 11 for k in range(1000)]
before = [owner(servers, k1) for k1 in keys]
print(f"1000 keys on 5 servers: {loads(servers, before)}")
gone = "charlie"
fewer = [s for s in servers if s != gone]
after = [owner(fewer, k2) for k2 in keys]
moved = 0
innocent = 0
for i in range(len(keys)):
    if before[i] != after[i]:
        moved += 1
        if before[i] != gone:
            innocent += 1
print(f"charlie leaves: {moved} keys move, {innocent} of them were not on charlie")
print(f"now: {loads(fewer, after)}")
more = list(servers)
more.append("foxtrot")
grown = [owner(more, k3) for k3 in keys]
taken = [i for i in range(len(keys)) if grown[i] != before[i]]
to_new = len([i for i in taken if grown[i] == "foxtrot"])
print(f"foxtrot joins: {len(taken)} keys move, {to_new} of them to foxtrot")

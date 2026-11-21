def picked(spec, n):
    keep = set()
    for part in spec.split(","):
        dash = part.find("-")
        lo = 1
        hi = n
        if dash < 0:
            lo = int(part)
            hi = lo
        else:
            if dash > 0:
                lo = int(part[:dash])
            if dash + 1 < len(part):
                hi = int(part[dash + 1:])
        for p in range(lo, min(hi, n) + 1):
            keep.add(p)
    return sorted(keep)

rows = ["id:name:shell:home:uid", "1:root:/bin/sh:/root:0", "2:ana:/bin/zsh:/home/ana:1000", "3:ben:/bin/bash:/home/ben:1001"]
for spec in ["2", "1,3-4", "4-,1", "-2"]:
    print(f"-f {spec}")
    for r in rows[1:]:
        fields = r.split(":")
        idx = picked(spec, len(fields))
        print("  " + ":".join(fields[i - 1] for i in idx))
word = "2025-03-12T10:44:09"
cs = list(word)
chosen = [cs[i - 1] for i in picked("1-4,12-", len(cs))]
print(f"-c 1-4,12- {word} -> {''.join(chosen)}")

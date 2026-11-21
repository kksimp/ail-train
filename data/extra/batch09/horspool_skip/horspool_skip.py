def skip_table(p):
    m = len(p)
    shift = {}
    for i in range(m - 1):
        shift[p[i]] = m - 1 - i
    return shift

def search(t, p):
    m = len(p)
    shift = skip_table(p)
    pos = 0
    hits = []
    tries = 0
    looks = 0
    while pos + m <= len(t):
        tries += 1
        j = m - 1
        while j >= 0:
            looks += 1
            if t[pos + j] != p[j]:
                break
            j -= 1
        if j < 0:
            hits.append(pos)
        pos += shift.get(t[pos + m - 1], m)
    spots = "none" if not hits else ", ".join(str(h) for h in hits)
    print(f"{p:<9} hits {spots}; {tries} alignments, {looks} letter checks")

table = skip_table("example")
shown = " ".join(f"{k}={table[k]}" for k in sorted(table))
print(f"skips for 'example': {shown}, others 7")
text = "here is a simple example of an example text"
for pat in ["example", "simple", "ex", "plex"]:
    search(text, pat)

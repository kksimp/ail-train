def fits(rows, w):
    k = len(rows)
    for j in range(k):
        if rows[j][k] != w[j]:
            return False
    return True

def search(words, rows, found):
    if len(rows) == 4:
        found.append(" ".join(rows))
        return
    for w in words:
        if fits(rows, w):
            rows.append(w)
            search(words, rows, found)
            rows.pop()

words = ["ball", "area", "lead", "lady", "card", "acre", "rely", "dyes", "wall", "dear", "earl", "arts", "lest", "cake", "aloe", "kept", "eyes"]
rows = []
found = []
search(words, rows, found)
print(f"{len(found)} word squares from {len(words)} words")
for sq in found[:3]:
    print(sq)
for w in found[0].split(" "):
    print(f"  {w.upper()}")

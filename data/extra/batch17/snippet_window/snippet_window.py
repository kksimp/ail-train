def clean(w):
    return "".join(c for c in w.lower() if c.isalpha())

def mark(w, query):
    return f"[{w}]" if clean(w) in query else w

def snippet(text, query, size):
    words = text.split()
    best = 0
    best_score = -1
    for start in range(max(len(words) - size + 1, 1)):
        end = min(start + size, len(words))
        found = set()
        for w in words[start:end]:
            cw = clean(w)
            if cw in query:
                found.add(cw)
        if len(found) > best_score:
            best_score = len(found)
            best = start
    end = min(best + size, len(words))
    shown = [mark(w, query) for w in words[best:end]]
    pre = "... " if best > 0 else ""
    post = " ..." if end < len(words) else ""
    return f"{pre}{' '.join(shown)}{post}"

doc = "The library opens at nine. Members can borrow up to ten books, and the reading room stays quiet until noon. Late books cost a small fee per day, but children's books are free to renew online at any time."
for q in [["books", "renew"], ["reading", "quiet", "noon"], ["fee"], ["parking"]]:
    print(f"{' '.join(q)}:")
    print(f"  {snippet(doc, q, 8)}")

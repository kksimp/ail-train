def is_vowel(c):
    return c in "aeiou"

def first_cv(w):
    if is_vowel(w[0]):
        return w[0]
    return w[0] + w[1]

def first_cvc(w):
    cv = first_cv(w)
    n = len(cv)
    if n < len(w) and not is_vowel(w[n]):
        return cv + w[n]
    return cv

def redup(k, w):
    if k == "Full":
        return f"{w}-{w}"
    if k == "CvPrefix":
        return first_cv(w) + w
    return first_cvc(w) + w

data = [("Indonesian", "Full", "buku", "books"), ("Indonesian", "Full", "rumah", "houses"), ("Tagalog", "CvPrefix", "sulat", "will write"), ("Tagalog", "CvPrefix", "basa", "will read"), ("Tagalog", "CvPrefix", "inom", "will drink"), ("Ilocano", "CvcPrefix", "pusa", "cats"), ("Ilocano", "CvcPrefix", "kalding", "goats"), ("Ilocano", "CvcPrefix", "talon", "fields")]
added = 0
for lang, k, w, gloss in data:
    out = redup(k, w)
    added += len(out) - len(w)
    print(f"{lang:<10} {w:<8} -> {out:<14} '{gloss}'")
print(f"{added} letters added by copying")

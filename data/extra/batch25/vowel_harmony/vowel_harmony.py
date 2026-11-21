def last_vowel(word):
    v = 'e'
    for c in word:
        if c in "aeıioöuü":
            v = c
    return v

def two_way(v):
    return "e" if v in "eiöü" else "a"

def four_way(v):
    if v in "ei":
        return "i"
    if v in "aı":
        return "ı"
    if v in "ou":
        return "u"
    return "ü"

def locative(word):
    last = word[-1]
    first = "t" if last in "çfhkpsşt" else "d"
    return f"{word}{first}{two_way(last_vowel(word))}"

words = ["ev", "kitap", "göz", "okul", "köprü", "masa", "kalem", "ağaç", "kız", "gün"]
fronts = 0
for w in words:
    v = last_vowel(w)
    h = two_way(v)
    if h == "e":
        fronts += 1
    print(f"{w}: plural {w}l{h}r, locative {locative(w)}, question {w} m{four_way(v)}")
print(f"{fronts} front stems, {len(words) - fronts} back stems")

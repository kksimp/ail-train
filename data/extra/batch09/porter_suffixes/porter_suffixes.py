def cons(w, i):
    if w[i] in "aeiou":
        return False
    return w[i] != 'y' or i == 0 or not cons(w, i - 1)

def measure(w):
    m = 0
    prev_vowel = False
    for i in range(len(w)):
        v = not cons(w, i)
        if prev_vowel and not v:
            m += 1
        prev_vowel = v
    return m

def has_vowel(w):
    return any(c in "aeiou" for c in w)

def cvc(w):
    n = len(w)
    return n >= 3 and cons(w, n - 3) and not cons(w, n - 2) and cons(w, n - 1) and w[n - 1] not in "wxy"

def stem(word):
    w = word
    if w.endswith("sses") or w.endswith("ies"):
        w = w[:len(w) - 2]
    elif w.endswith("s") and not w.endswith("ss"):
        w = w[:len(w) - 1]
    cut = 0
    if w.endswith("ed") and has_vowel(w[:len(w) - 2]):
        cut = 2
    elif w.endswith("ing") and has_vowel(w[:len(w) - 3]):
        cut = 3
    if cut > 0:
        w = w[:len(w) - cut]
        n = len(w)
        if w.endswith("at") or w.endswith("bl") or w.endswith("iz"):
            w = w + "e"
        elif n >= 2 and w[n - 1] == w[n - 2] and cons(w, n - 1) and w[n - 1] not in "lsz":
            w = w[:n - 1]
        elif measure(w) == 1 and cvc(w):
            w = w + "e"
    if w.endswith("y") and has_vowel(w[:len(w) - 1]):
        w = w[:len(w) - 1] + "i"
    return w

words = ["caresses", "ponies", "cats", "running", "plastered", "motoring", "sing", "conflated", "troubled", "sized", "hopping", "tanned", "falling", "hissing", "filing", "happy", "sky", "fizzed", "bled", "toys"]
for i in range(0, len(words), 4):
    print(", ".join(f"{w} -> {stem(w)}" for w in words[i:i + 4]))

initials = ["g", "kk", "n", "d", "tt", "r", "m", "b", "pp", "s", "ss", "", "j", "jj", "ch", "k", "t", "p", "h"]
vowels = ["a", "ae", "ya", "yae", "eo", "e", "yeo", "ye", "o", "wa", "wae", "oe", "yo", "u", "wo", "we", "wi", "yu", "eu", "ui", "i"]
finals = ["", "k", "k", "k", "n", "n", "n", "t", "l", "k", "m", "p", "l", "l", "p", "l", "m", "p", "p", "t", "t", "ng", "t", "t", "k", "t", "p", "t"]

def romanise(word):
    parts = []
    for c in word:
        s = ord(c) - 0xAC00
        l = s // (21 * 28)
        v = s % (21 * 28) // 28
        t = s % 28
        parts.append(f"{initials[l]}{vowels[v]}{finals[t]}")
    return "-".join(parts)

def jamo(word):
    parts = []
    for c in word:
        s = ord(c) - 0xAC00
        parts.append(f"({s // 588},{s % 588 // 28},{s % 28})")
    return " ".join(parts)

def compose(l, v, t):
    return chr(0xAC00 + (l * 21 + v) * 28 + t)

for w in ["한국어", "서울", "김치", "사랑", "음악", "바다"]:
    print(f"{w}: {romanise(w)} {jamo(w)}")
built = compose(18, 0, 4) + compose(0, 8, 8)
print(f"built from (18,0,4) (0,8,8): {built}")
print(f"blocks in all: {19 * 21 * 28}")

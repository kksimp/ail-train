def vowel(c):
    return c in "aeiou"

def ing(verb):
    n = len(verb)
    last = verb[n - 1]
    if verb.endswith("ie"):
        return verb[:n - 2] + "ying"
    if last == 'e' and n > 2 and verb[n - 2] not in "eyo":
        return verb[:n - 1] + "ing"
    if last == 'c':
        return verb + "king"
    vowels = sum(1 for c in verb if vowel(c))
    if n >= 3 and vowels == 1 and not vowel(last) and vowel(verb[n - 2]) and not vowel(verb[n - 3]) and last not in "wxy":
        return verb + last + "ing"
    return verb + "ing"

verbs = ["make", "die", "lie", "see", "run", "swim", "panic", "play", "fix", "agree", "dye", "toe", "open", "sit", "write", "picnic"]
for i in range(0, len(verbs), 4):
    print(", ".join(f"{v} -> {ing(v)}" for v in verbs[i:i + 4]))
doubled = [v for v in verbs if len(ing(v)) == len(v) + 4]
print("verbs that grow by a letter: " + " ".join(doubled))

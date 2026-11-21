def vowel(c):
    return c in "aeiou"

def past(verb):
    irregular = {"go": "went", "eat": "ate", "see": "saw", "take": "took", "run": "ran", "write": "wrote", "drive": "drove"}
    if verb in irregular:
        return irregular[verb]
    n = len(verb)
    last = verb[n - 1]
    if last == 'e':
        return verb + "d"
    if last == 'y' and not vowel(verb[n - 2]):
        return verb[:n - 1] + "ied"
    vowels = sum(1 for c in verb if vowel(c))
    short = n >= 3 and vowels == 1 and not vowel(last) and vowel(verb[n - 2]) and not vowel(verb[n - 3])
    if short and last not in "wxy":
        return verb + last + "ed"
    return verb + "ed"

verbs = ["walk", "bake", "cry", "play", "stop", "plan", "rain", "fix", "visit", "go", "write", "hop", "hope", "study"]
for i in range(0, len(verbs), 5):
    row = verbs[i:i + 5]
    print("  ".join(f"{v}/{past(v)}" for v in row))
story = ["plan", "pack", "drive", "stop", "eat", "carry", "relax"]
told = ", ".join(past(v) for v in story)
print(f"yesterday we {told}")

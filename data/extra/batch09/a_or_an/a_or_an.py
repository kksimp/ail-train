def article(word):
    lower = word.lower()
    if len(word) > 1 and all(c.isupper() for c in word):
        return "an" if word[0] in "AEFHILMNORSX" else "a"
    for p in ["uni", "use", "eu", "one", "once"]:
        if lower.startswith(p):
            return "a"
    for p in ["hour", "honest", "heir", "honour"]:
        if lower.startswith(p):
            return "an"
    return "an" if lower[0] in "aeiou" else "a"

words = ["apple", "banana", "hour", "house", "umbrella", "unicorn", "user", "European", "one-off", "honest", "FBI", "UFO", "LED", "MRI", "egg", "heir"]
parts = [f"{article(w)} {w}" for w in words]
for i in range(0, len(parts), 4):
    print(", ".join(parts[i:i + 4]))
an_count = sum(1 for w in words if article(w) == "an")
print(f"{an_count} of {len(words)} take an")

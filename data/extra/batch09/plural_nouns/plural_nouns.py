def plural(word):
    irregular = {"child": "children", "mouse": "mice", "person": "people", "foot": "feet", "sheep": "sheep", "tooth": "teeth"}
    if word in irregular:
        return irregular[word]
    n = len(word)
    last = word[n - 1]
    before = word[n - 2]
    if last in "sxz" or word.endswith("ch") or word.endswith("sh"):
        return word + "es"
    if last == 'y' and before not in "aeiou":
        return word[:n - 1] + "ies"
    if word in ["knife", "leaf", "wolf", "life", "half", "shelf"]:
        stem = word[:n - 2] if last == 'e' else word[:n - 1]
        return stem + "ves"
    if word in ["potato", "hero", "tomato", "echo"]:
        return word + "es"
    return word + "s"

def count_of(n, word):
    shown = word if n == 1 else plural(word)
    return f"{n} {shown}"

words = ["box", "church", "baby", "day", "knife", "roof", "potato", "photo", "child", "sheep", "bus", "wolf"]
parts = [f"{w} -> {plural(w)}" for w in words]
for i in range(0, len(parts), 4):
    print(", ".join(parts[i:i + 4]))
print(f"{count_of(1, 'mouse')}, {count_of(3, 'mouse')}, {count_of(2, 'tooth')}, {count_of(5, 'fox')}")

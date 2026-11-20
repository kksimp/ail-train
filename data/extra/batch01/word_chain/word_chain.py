def check(words):
    used = set()
    prev = ""
    for w in words:
        if w in used:
            return f"'{w}' was used twice"
        used.add(w)
        if prev and prev[-1] != w[0]:
            return f"'{w}' does not start with the end of '{prev}'"
        prev = w
    return "valid chain"
games = [["apple", "egg", "giraffe", "eel", "lemon"], ["tree", "eagle", "eagle"], ["sun", "night", "tiger", "rose", "moon"], []]
for g in games:
    print(f"{len(g)} words: {check(g)}")
best = games[0][0]
for w in games[0]:
    if len(w) > len(best):
        best = w
print(f"longest word: {best}")

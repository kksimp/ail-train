def profile(text, keep):
    counts = {}
    for w in text.lower().split():
        cs = "_" + w + "_"
        for i in range(len(cs) - 2):
            g = cs[i:i + 3]
            counts[g] = counts.get(g, 0) + 1
    keys = sorted(counts.keys(), key=lambda k: (-counts[k], k))
    return keys[:min(keep, len(keys))]

def distance(doc, lang):
    d = 0
    for i, g in enumerate(doc):
        if g in lang:
            d += abs(i - lang.index(g))
        else:
            d += len(lang)
    return d

names = ["English", "Spanish", "German"]
samples = ["the quick brown fox jumps over the lazy dog and the cat sat on the mat while the children were playing in the garden with their friends there is nothing that they would rather do than this", "el perro come la comida en la casa de su madre y los chicos juegan en el jardin con sus amigos todos los dias porque les gusta mucho estar juntos en la calle", "der hund isst das essen in dem haus seiner mutter und die kinder spielen mit ihren freunden in dem garten jeden tag weil sie gerne zusammen sind auf der strasse"]
profiles = [profile(s, 60) for s in samples]
tests = ["the children and the dog", "los perros de la casa", "die kinder und der hund", "they were in the garden", "con sus amigos en la calle", "spielen sie in dem garten"]
for t in tests:
    doc = profile(t, 60)
    scores = [distance(doc, p) for p in profiles]
    best = 0
    for i in range(1, len(scores)):
        if scores[i] < scores[best]:
            best = i
    shown = "[" + ", ".join(str(x) for x in scores) + "]"
    print(f"{t:<27} {shown} -> {names[best]}")

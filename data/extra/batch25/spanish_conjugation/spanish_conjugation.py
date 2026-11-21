endings = {"ar": ["o", "as", "a", "amos", "áis", "an"], "er": ["o", "es", "e", "emos", "éis", "en"], "ir": ["o", "es", "e", "imos", "ís", "en"]}

def conjugate(inf, change, person):
    n = len(inf)
    stem = inf[:n - 2]
    group = inf[n - 2:]
    if change != "" and person != 3 and person != 4:
        target = "e" if change == "ie" else "o"
        i = stem.rfind(target)
        if i >= 0:
            stem = stem[:i] + change + stem[i + 1:]
    return stem + endings[group][person]

verbs = [("hablar", ""), ("comer", ""), ("vivir", ""), ("pensar", "ie"), ("querer", "ie"), ("preferir", "ie"), ("dormir", "ue"), ("contar", "ue")]
changed = 0
for inf, change in verbs:
    forms = [conjugate(inf, change, p) for p in range(6)]
    if change != "":
        changed += 4
    shown = ", ".join(forms)
    print(f"{inf:<9} {shown}")
print(f"{changed} forms with a changed stem")

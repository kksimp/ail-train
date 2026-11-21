def initials(given):
    out = []
    for g in given:
        pieces = [p[:1].upper() + "." for p in g.split("-")]
        out.append("-".join(pieces))
    return " ".join(out)

def surname_start(words):
    for i in range(1, len(words)):
        if words[i][:1].islower():
            return i
    return len(words) - 1

def surname(name):
    words = name.split(" ")
    return " ".join(words[surname_start(words):])

def reference_name(name):
    words = name.split(" ")
    at = surname_start(words)
    return f"{' '.join(words[at:])}, {initials(words[:at])}"

def reference_list(names):
    refs = [reference_name(n) for n in names]
    if len(refs) == 1:
        return refs[0]
    return f"{', '.join(refs[:-1])}, & {refs[-1]}"

def in_text(names, year):
    if len(names) == 1:
        return f"({surname(names[0])}, {year})"
    if len(names) == 2:
        return f"({surname(names[0])} & {surname(names[1])}, {year})"
    return f"({surname(names[0])} et al., {year})"

works = [(["Ada King Lovelace"], 1843), (["Guido van Rossum", "Fred L. Drake"], 2009), (["Jean-Paul Sartre"], 1943), (["Donald Ervin Knuth", "James H. Morris", "Vaughan Pratt"], 1977), (["Ludwig van Beethoven", "Carl de la Cruz"], 1801)]
for names, year in works:
    print(f"{reference_list(names)} ({year}).")
    print(f"    cited as {in_text(names, year)}")

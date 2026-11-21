data = [("English", "the_dog/S chased/V the_cat/O"), ("English", "Mary/S reads/V books/O"), ("Japanese", "Taroo-ga/S hon-o/O yonda/V"), ("Japanese", "neko-ga/S sakana-o/O tabeta/V"), ("Irish", "chonaic/V Seán/S an_madra/O"), ("Irish", "léann/V Máire/S leabhair/O"), ("Malagasy", "mamaky/V boky/O ny_mpianatra/S"), ("Turkish", "Ali/S elmayı/O yedi/V"), ("Turkish", "elmayı/O Ali/S yedi/V"), ("Turkish", "kız/S kitabı/O okudu/V")]

def order(text):
    tags = []
    for chunk in text.split(" "):
        parts = chunk.split("/")
        if len(parts) == 2:
            tags.append(parts[1])
    return "".join(tags)

def position(o):
    if o.startswith("V"):
        return "verb-initial"
    if o.endswith("V"):
        return "verb-final"
    return "verb-medial"

langs = []
counts = {}
for lang, text in data:
    if lang not in langs:
        langs.append(lang)
    k = f"{lang} {order(text)}"
    counts[k] = counts.get(k, 0) + 1
for l in langs:
    best = ""
    most = 0
    seen = 0
    for key, n in counts.items():
        if key.startswith(l + " "):
            seen += 1
            if n > most:
                most = n
                best = key[len(l) + 1:]
    total = len([1 for s in data if s[0] == l])
    print(f"{l:<9} {best} ({most} of {total} sentences, {seen} orders seen), {position(best)}")

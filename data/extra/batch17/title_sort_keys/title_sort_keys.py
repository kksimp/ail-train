def sort_key(title):
    articles = ["the ", "a ", "an ", "le ", "la ", "les ", "der ", "die ", "das ", "el "]
    t = title.lower()
    for a in articles:
        if t.startswith(a):
            t = t[len(a):]
            break
    if t.startswith("l'"):
        t = t[2:]
    kept = [c for c in t if c not in "\"'.,:;!?"]
    return "".join(kept).strip()

titles = ["The Hobbit", "A Tale of Two Cities", "Le Petit Prince", "L'Avare", "Die Verwandlung", "Anna Karenina", "\"Ulysses\"", "El Aleph", "Les Miserables", "Animal Farm", "Das Kapital", "1984"]
ordered = sorted(titles, key=sort_key)
for t in ordered:
    print(f"{sort_key(t):<22} {t}")
moved = len([t for t in titles if not t.lower().startswith(sort_key(t)[:3])])
print(f"{moved} titles have a key that differs from how they start")

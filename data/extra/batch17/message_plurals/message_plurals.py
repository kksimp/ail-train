def form_of(lang, n):
    last = n % 10
    last2 = n % 100
    few = last >= 2 and last <= 4 and (last2 < 12 or last2 > 14)
    if lang == "en":
        return "One" if n == 1 else "Other"
    if lang == "fr":
        return "One" if n <= 1 else "Other"
    if lang == "ru":
        return "One" if last == 1 and last2 != 11 else "Few" if few else "Many"
    if lang == "pl":
        return "One" if n == 1 else "Few" if few else "Many"
    return "Other"

def word(lang, f):
    words = {"en": ["file", "files", "files"], "fr": ["fichier", "fichiers", "fichiers"], "ru": ["файл", "файла", "файлов"]}.get(lang, ["plik", "pliki", "plików"])
    return {"One": words[0], "Few": words[1], "Many": words[2], "Other": words[1]}[f]

for n in [0, 1, 2, 5, 11, 21, 22, 112]:
    parts = []
    for lang in ["en", "fr", "ru", "pl"]:
        w = word(lang, form_of(lang, n))
        cell = f"{n} {w}"
        parts.append(cell.ljust(14, ' '))
    print("".join(parts).rstrip())
print(f"ru 21 is {form_of('ru', 21)}, pl 21 is {form_of('pl', 21)}")

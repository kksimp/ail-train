def transliterate(s):
    lower = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
    upper = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
    table = ["a", "b", "v", "g", "d", "e", "e", "zh", "z", "i", "i", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u", "f", "kh", "ts", "ch", "sh", "shch", "ie", "y", "", "e", "iu", "ia"]
    out = []
    for c in s:
        if c in lower:
            out.append(table[lower.index(c)])
        elif c in upper:
            t = table[upper.index(c)]
            out.append(t[:1].upper() + t[1:])
        else:
            out.append(c)
    return "".join(out)

names = ["Москва", "Санкт-Петербург", "Чайковский", "Юрий Гагарин", "Щёлково", "Хабаровск", "Ольга", "Нижний Новгород"]
for n in names:
    t = transliterate(n)
    print(f"{n:<16} {t}")
print(f"letters before and after: {sum(len(n) for n in names)} -> {sum(len(transliterate(n)) for n in names)}")

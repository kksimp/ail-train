def fold(s):
    from_chars = "àáâãåçèéêëìíîïñòóôõøùúûýÿÀÁÂÃÅÇÈÉÊËÌÍÎÏÑÒÓÔÕØÙÚÛÝ"
    to_chars = "aaaaaceeeeiiiinooooouuuyyaaaaaceeeeiiiinooooouuuy"
    out = []
    for c in s:
        if c in from_chars:
            out.append(to_chars[from_chars.index(c)])
        elif c == 'ä' or c == 'Ä':
            out.append("ae")
        elif c == 'ö' or c == 'Ö':
            out.append("oe")
        elif c == 'ü' or c == 'Ü':
            out.append("ue")
        elif c == 'ß':
            out.append("ss")
        else:
            out.append(c)
    return "".join(out).lower()

titles = ["Crème Brûlée", "Smörgåsbord Guide", "Über den Fluß", "São Paulo Nights", "Café Society", "Ñandú Tales", "Dvořák Symphonies"]
for t in titles:
    print(f"{t:<19} -> {fold(t)}")
for q in ["creme", "uber", "fluss", "sao", "CAFE", "nandu", "dvorak"]:
    hits = [t for t in titles if fold(q) in fold(t)]
    shown = "(no match)" if len(hits) == 0 else ", ".join(hits)
    print(f"search {q:<7} {shown}")

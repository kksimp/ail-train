def weekday(y, m, d):
    t = [0, 3, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4]
    yy = y - 1 if m < 3 else y
    return (yy + yy // 4 - yy // 100 + yy // 400 + t[m - 1] + d) % 7

def names(lang):
    if lang == "de":
        return [["Sonntag", "Montag", "Dienstag", "Mittwoch", "Donnerstag", "Freitag", "Samstag"], ["Januar", "Februar", "März", "April", "Mai", "Juni", "Juli", "August", "September", "Oktober", "November", "Dezember"]]
    if lang == "fr":
        return [["dimanche", "lundi", "mardi", "mercredi", "jeudi", "vendredi", "samedi"], ["janvier", "février", "mars", "avril", "mai", "juin", "juillet", "août", "septembre", "octobre", "novembre", "décembre"]]
    if lang == "es":
        return [["domingo", "lunes", "martes", "miércoles", "jueves", "viernes", "sábado"], ["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"]]
    return [["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"], ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]]

def long_form(loc, y, m, d):
    nm = names(loc[:2])
    wd = nm[0][weekday(y, m, d)]
    mon = nm[1][m - 1]
    if loc == "en-US":
        return f"{wd}, {mon} {d}, {y}"
    if loc == "en-GB":
        return f"{wd} {d} {mon} {y}"
    if loc == "de-DE":
        return f"{wd}, {d}. {mon} {y}"
    if loc == "fr-FR":
        return f"{wd} {d} {mon} {y}"
    return f"{wd}, {d} de {mon} de {y}"

def short_form(loc, y, m, d):
    if loc == "en-US":
        return f"{m}/{d}/{y}"
    if loc == "de-DE":
        return f"{d:02}.{m:02}.{y}"
    if loc == "es-ES":
        return f"{d}/{m}/{y}"
    return f"{d:02}/{m:02}/{y}"

dates = [[2025, 3, 7], [2024, 12, 25]]
for dt in dates:
    y, m, d = dt
    for loc in ["en-US", "en-GB", "de-DE", "fr-FR", "es-ES"]:
        print(f"{loc} {short_form(loc, y, m, d):<10} {long_form(loc, y, m, d)}")

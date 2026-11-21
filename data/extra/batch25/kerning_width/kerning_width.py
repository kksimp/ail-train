def width(word, adv, kern):
    plain = 0
    kerned = 0
    for i in range(len(word)):
        a = adv.get(word[i], 600)
        plain += a
        kerned += a
        if i + 1 < len(word):
            kerned += kern.get(word[i] + word[i + 1], 0)
    return (plain, kerned)

adv = {'A': 667, 'V': 667, 'W': 944, 'T': 611, 'Y': 667, 'L': 556, 'o': 556, 'a': 556, 'y': 500, 'e': 556, 'r': 333, 'v': 500, 'P': 667, 'g': 556, 'l': 222}
kern = {"AV": -80, "VA": -80, "AW": -60, "WA": -60, "To": -70, "Ta": -70, "Ty": -60, "LT": -90, "LY": -100, "Yo": -90, "Pa": -40, "Tr": -50, "Va": -60, "ay": -20}
words = ["AVATAR", "Toyota", "WAVY", "LYTTLE", "Paley", "Travel", "Vegan"]
box = 300
for w in words:
    plain, kerned = width(w, adv, kern)
    saved = (plain - kerned) / plain * 100.0
    px = kerned * 24.0 / 1000.0
    fit = box * 1000 // kerned
    print(f"{w:<7} {plain:>5} -> {kerned:>5} units ({saved:.1f}% tighter), {px:.1f} px at 24, fits {box} px up to {fit} px")

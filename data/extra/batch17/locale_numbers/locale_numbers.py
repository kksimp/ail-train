class Locale:
    def __init__(self, tag, group, decimal, places, symbol, before):
        self.tag, self.group, self.decimal, self.places, self.symbol, self.before = tag, group, decimal, places, symbol, before

def grouped(n, sep):
    digits = str(n)
    parts = []
    end = len(digits)
    while end > 3:
        parts.insert(0, digits[end - 3:end])
        end -= 3
    parts.insert(0, digits[:end])
    return sep.join(parts)

def money(cents, loc):
    neg = cents < 0
    a = abs(cents)
    if loc.places == 0:
        body = grouped((a + 50) // 100, loc.group)
    else:
        body = f"{grouped(a // 100, loc.group)}{loc.decimal}{a % 100:02}"
    sign = "-" if neg else ""
    if loc.before:
        return f"{sign}{loc.symbol}{body}"
    return f"{sign}{body} {loc.symbol}"

locales = [Locale("en-US", ",", ".", 2, "$", True), Locale("de-DE", ".", ",", 2, "€", False), Locale("fr-FR", " ", ",", 2, "€", False), Locale("de-CH", "'", ".", 2, "CHF ", True), Locale("ja-JP", ",", ".", 0, "¥", True)]
amounts = [123456789, 99, -450075, 100000]
for loc in locales:
    cells = [money(c, loc) for c in amounts]
    shown = "".join(c.rjust(17, ' ') for c in cells)
    print(f"{loc.tag}{shown}")

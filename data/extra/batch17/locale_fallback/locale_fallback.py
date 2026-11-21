def chain(locale):
    out = [locale]
    lang = locale.split("-")[0]
    if lang != locale:
        out.append(lang)
    if lang != "en":
        out.append("en")
    return out

def lookup(catalog, locale, key):
    for loc in chain(locale):
        k = f"{loc}:{key}"
        if k in catalog:
            return f"{catalog[k]} [{loc}]"
    return f"<{key}?>"

catalog = {"en:hello": "Hello", "en:cart": "Your basket", "en:bye": "Goodbye", "de:hello": "Hallo", "de:cart": "Warenkorb", "de-AT:hello": "Servus", "fr:hello": "Bonjour", "fr:bye": "Au revoir", "fr-CA:cart": "Panier", "pt:hello": "Olá"}
users = ["de-AT", "de-CH", "fr-CA", "pt-BR", "en-GB"]
for u in users:
    parts = [lookup(catalog, u, k) for k in ["hello", "cart", "bye"]]
    shown = " | ".join(parts)
    print(f"{u:<6} {shown}")
missing = [k for k in ["hello", "cart", "bye", "help"] if f"en:{k}" not in catalog]
print(f"keys missing from English: {len(missing)}")
print(lookup(catalog, "de-AT", "help"))

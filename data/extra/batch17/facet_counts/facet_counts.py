class Item:
    def __init__(self, name, brand, colour, price):
        self.name, self.brand, self.colour, self.price = name, brand, colour, price

def band(p):
    return "under 50" if p < 50 else "50-99" if p < 100 else "100+"

def keep(it, brands, colours, skip):
    brand_ok = skip == "brand" or len(brands) == 0 or it.brand in brands
    colour_ok = skip == "colour" or len(colours) == 0 or it.colour in colours
    return brand_ok and colour_ok

items = [Item("trail", "Acme", "red", 80), Item("city", "Acme", "black", 45), Item("sprint", "Bolt", "red", 120), Item("cloud", "Bolt", "white", 95), Item("hike", "Crest", "black", 60), Item("lite", "Crest", "red", 30), Item("pro", "Acme", "white", 150)]
brands = ["Acme", "Bolt"]
colours = ["red"]
shown = ", ".join(it.name for it in items if keep(it, brands, colours, ""))
print(f"results: {shown}")
by_brand = {}
by_colour = {}
by_band = {}
for it in items:
    if keep(it, brands, colours, "brand"):
        by_brand[it.brand] = by_brand.get(it.brand, 0) + 1
    if keep(it, brands, colours, "colour"):
        by_colour[it.colour] = by_colour.get(it.colour, 0) + 1
    if keep(it, brands, colours, ""):
        by_band[band(it.price)] = by_band.get(band(it.price), 0) + 1
for b in sorted(by_brand.keys()):
    tick = "[x]" if b in brands else "[ ]"
    print(f"brand  {tick} {b:<6} {by_brand[b]}")
for c in sorted(by_colour.keys()):
    tick = "[x]" if c in colours else "[ ]"
    print(f"colour {tick} {c:<6} {by_colour[c]}")
for p, n in by_band.items():
    print(f"price      {p:<8} {n}")

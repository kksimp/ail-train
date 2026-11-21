def qty(t):
    try:
        n = int(t)
    except ValueError:
        return None, f"'{t}' is not a whole number"
    if n <= 0: return None, "quantity must be positive"
    return n, None
def read_line(l):
    p = l.split(" g ")
    if len(p) != 2: return None, f"expected 'N g name' in '{l}'"
    g, e = qty(p[0].strip())
    if e: return None, e
    return (p[1].strip(), g), None
cards = [("shortbread", ["200 g flour", "50 g sugar", "120 g butter"]), ("risotto", ["300 g rice", "x g peas"]), ("bread", ["500 g flour", "250 water"]), ("brine", ["0 g salt"])]
for name, lines in cards:
    items = []; err = None
    for l in lines:
        it, e = read_line(l)
        if e: err = e; break
        items.append(it)
    if err:
        print(f"{name}: rejected, {err}"); continue
    tot = sum(i[1] for i in items)
    h = items[0]
    for i in items:
        if i[1] > h[1]: h = i
    print(f"{name}: {len(items)} items, {tot} g, mostly {h[0]}")

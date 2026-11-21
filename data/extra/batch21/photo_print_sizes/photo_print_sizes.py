def crop(long, short):
    if long * 4000 >= short * 6000:
        return [6000, 6000 * short // long]
    return [4000 * long // short, 4000]

def quality(ppi):
    return "excellent" if ppi >= 300 else ("good" if ppi >= 200 else "poor")

largest = ""
for long, short in [(6, 4), (7, 5), (10, 8), (12, 8), (15, 10), (20, 16), (30, 20), (36, 24)]:
    c = crop(long, short)
    ppi = c[0] // long
    kept = c[0] * c[1] * 100 // 24000000
    if ppi >= 200:
        largest = f"{long}x{short}"
    print(f"{long:>2}x{short:<2} in: crop {c[0]}x{c[1]} ({kept}% kept), {ppi} ppi, {quality(ppi)}")
print(f"largest good print: {largest}")

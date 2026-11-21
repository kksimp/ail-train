ALPHABET = "0123456789bcdefghjkmnpqrstuvwxyz"

def encode(lat, lon, chars):
    lat_lo, lat_hi = -90.0, 90.0
    lon_lo, lon_hi = -180.0, 180.0
    out = []
    bits = 0
    value = 0
    even = True
    while len(out) < chars:
        if even:
            mid = (lon_lo + lon_hi) / 2.0
            value = value * 2 + (1 if lon >= mid else 0)
            if lon >= mid:
                lon_lo = mid
            else:
                lon_hi = mid
        else:
            mid = (lat_lo + lat_hi) / 2.0
            value = value * 2 + (1 if lat >= mid else 0)
            if lat >= mid:
                lat_lo = mid
            else:
                lat_hi = mid
        even = not even
        bits += 1
        if bits == 5:
            out.append(ALPHABET[value])
            bits = 0
            value = 0
    return "".join(out)

def shared(a, b):
    n = 0
    while n < len(a) and n < len(b) and a[n] == b[n]:
        n += 1
    return n

places = [("Eiffel Tower", 48.8584, 2.2945), ("Louvre", 48.8606, 2.3376), ("Notre-Dame", 48.853, 2.3499), ("Big Ben", 51.5007, -0.1246), ("Statue of Liberty", 40.6892, -74.0445), ("Christ the Redeemer", -22.9519, -43.2105)]
hashes = []
for name, lat, lon in places:
    h = encode(lat, lon, 8)
    hashes.append(h)
    print(f"{name:<20} {h}")
for j in range(1, len(places)):
    print(f"{places[0][0]} and {places[j][0]} share {shared(hashes[0], hashes[j])} characters")

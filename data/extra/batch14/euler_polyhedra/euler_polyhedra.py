names = {"3,3": "tetrahedron", "4,3": "cube", "3,4": "octahedron", "5,3": "dodecahedron", "3,5": "icosahedron"}
found = 0
for p in range(3, 7):
    for q in range(3, 7):
        den = 4 - (p - 2) * (q - 2)
        if den <= 0:
            continue
        e = 2 * p * q // den
        v, f = 2 * e // q, 2 * e // p
        found += 1
        nm = names.get(f"{p},{q}", "?")
        print(f"{{{p},{q}}} {nm:<12} V {v:>2} E {e:>2} F {f:>2} V-E+F {v - e + f}")
print(f"{found} regular solids")
sol = [(f"5-gon prism", 10, 15, 7), ("8-gon prism", 16, 24, 10), ("4x6 torus mesh", 24, 48, 24)]
for nm, v, e, f in sol:
    print(f"{nm:<16} V {v:>2} E {e:>2} F {f:>2} V-E+F {v - e + f}")

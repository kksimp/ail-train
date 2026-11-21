sites = [("Retail Park", "CCS", 0, 2), ("Hotel", "Type2", 2, 5), ("Motorway Services", "CCS", 3, 11), ("Town Hall", "CCS", 1, 7), ("Garage", "CHAdeMO", 1, 26)]
for plug, r in [("CCS", 15), ("Type2", 4), ("CHAdeMO", 30), ("Type2", 10)]:
    c = [s for s in sites if s[1] == plug and s[2] > 0 and s[3] <= r]
    if c:
        b = min(c, key=lambda s: s[3]); print(f"{plug} within {r} km: {b[0]} ({b[3]} km, {b[2]} free)")
    else: print(f"{plug} within {r} km: none")
print("full right now: [" + ", ".join(f'"{s[0]}"' for s in sites if s[2] == 0) + "]")

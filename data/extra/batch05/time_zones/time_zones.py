O = [("London", 0), ("Lagos", 1), ("Dubai", 4), ("Delhi", 5), ("Tokyo", 9), ("New York", -5)]
B = [sum(1 for _, o in O if 9 <= (h + o + 24) % 24 < 17) for h in range(24)]; b = max(B)
print(f"best: {b} of {len(O)} offices at " + ", ".join(f"{h:02}:00" for h in range(24) if B[h] == b))
for n, o in O: print(f"13:00 UTC is {(13 + o + 24) % 24:02}:00 in {n}")

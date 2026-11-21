ch = {"ana", "ben", "cai", "dev", "eli"}; dr = {"ben", "dev", "fay", "gus"}; co = {"ana", "ben", "dev", "fay", "hal"}
P = sorted(ch | dr | co)
q = lambda xs: "[" + ", ".join(f'"{x}"' for x in xs) + "]"
print(f"in all three: {q([p for p in P if p in ch and p in dr and p in co])}")
print(f"in exactly one: {q([p for p in P if sum(p in c for c in [ch, dr, co]) == 1])}")
print(f"chess not drama: {q([p for p in P if p in ch and p not in dr])}")
print(f"{len(P)} people in total")

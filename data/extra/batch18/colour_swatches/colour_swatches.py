A = [("Harbour Fog", 176, 196, 202), ("Clay", 186, 112, 78), ("Moss", 96, 120, 64), ("Chalk", 240, 236, 226)]
B = [("Sea Mist", 176, 196, 202), ("Terracotta", 190, 110, 80), ("Old Linen", 240, 236, 226)]
def hx(p): return f"#{p[1]:02x}{p[2]:02x}{p[3]:02x}"
for p in B:
    m = [a for a in A if a[1:] == p[1:]]
    if m: print(f"{p[0]} {hx(p)} = {m[0][0]}")
    else: print(f"{p[0]} {hx(p)}: no twin")
both = A + B
print(f"Chalk appears {sum(1 for x in both if x[1:] == A[3][1:])} times across both ranges")
print("same name, other colour: false")

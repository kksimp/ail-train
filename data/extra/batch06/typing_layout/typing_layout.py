def ro(c): return 1 if c in "qwertyuiop" else 2 if c in "asdfghjkl" else 3
B = ["", "", "", ""]
for w in ["typewriter", "flask", "zebra", "pottery", "salads", "proprietor", "gas", "mix", "rupture", "flags"]:
    r = {ro(c) for c in w}
    if len(r) == 1:
        r = r.pop(); print(f"{w}: row {r}")
        if len(w) > len(B[r]): B[r] = w
    else: print(f"{w}: mixed")
for r in range(1, 4): print(f"longest on row {r}: {B[r] or 'none'}")

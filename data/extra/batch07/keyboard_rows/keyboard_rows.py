def ro(c): return 1 if c in "qwertyuiop" else 2 if c in "asdfghjkl" else 3
B = ["", "", "", ""]
for w in ["typewriter", "alaska", "dad", "peace", "rupture", "flask", "proprietor", "zxcv", "mom", "gaffs", "pottery", "quiet", "hello"]:
    R = [ro(c) for c in w]
    if all(x == R[0] for x in R):
        print(f"{w}: row {R[0]}")
        if len(w) > len(B[R[0]]): B[R[0]] = w
for r in range(1, 4): print(f"longest on row {r}: {B[r] if B[r] else 'none'}")

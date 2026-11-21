for r in range(6): print("".join(f"{(r + 1) * (c + 1):>3}" for c in range(6)))
B = [["."] * 3 for _ in range(3)]; B[0][0] = "X"; B[1][1] = "O"; B[2][0] = "X"; B[1][0] = "O"
for r in B: print(" ".join(r))
print(f"corners {6 * 6 + 1 * 1}")

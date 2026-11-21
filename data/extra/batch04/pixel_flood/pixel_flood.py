I = [list(r) for r in ["..##....", ".#..#...", ".#...#..", "..#..#..", "...##...", "........"]]
for r in I: print("".join(r))
o = I[2][3]; st = [(2, 3)]; f = 0
while st:
    r, c = st.pop()
    if r < 0 or r >= len(I) or c < 0 or c >= len(I[0]) or I[r][c] != o: continue
    I[r][c] = "o"; f += 1; st += [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]
print("--")
for r in I: print("".join(r))
print(f"filled {f}")

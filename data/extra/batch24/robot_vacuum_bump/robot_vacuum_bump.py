room = ["##########", "#........#", "#..##....#", "#..##..#.#", "#.......##", "#.##.....#", "#........#", "##########"]
dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
r = 1; c = 1; d = 0; bumps = 0
clean = {r * 10 + c}
for step in range(1, 151):
    nr = r + dirs[d][0]; nc = c + dirs[d][1]
    if room[nr][nc] == '#':
        d = (d + [1, 2, 3][bumps % 3]) % 4
        bumps += 1
    else:
        r = nr; c = nc
        clean.add(r * 10 + c)
    if step == 50 or step == 100:
        print(f"after {step} moves: {len(clean)} cells clean")
floor = sum(line.count(".") for line in room)
for i in range(len(room)):
    print("".join('#' if room[i][j] == '#' else 'o' if (i * 10 + j) in clean else '-' for j in range(10)))
print(f"{len(clean)} of {floor} floor cells cleaned, {bumps} bumps")

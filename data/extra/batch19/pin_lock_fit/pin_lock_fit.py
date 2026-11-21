def heights(drawing):
    rows = drawing.split("/")
    h = [0] * 5
    for r in range(1, len(rows) - 1):
        for c, ch in enumerate(rows[r]):
            if ch == '#': h[c] += 1
    return h

locks = ["#####/.####/.####/.####/.#.#./.#.../.....", "#####/##.##/.#.##/...##/...#./...#./.....", "#####/####./#.##./#..#./#..../...../....."]
keys = ["...../#..../#..../#...#/#.#.#/#.###/#####", "...../..#../#.#../###../###.#/###.#/#####", "...../...../...../#..../#.#../#.#.#/#####", "...../....#/.#..#/.##.#/.####/#####/#####", "...../...../...../...../##..#/#####/#####"]
lh = [heights(d) for d in locks]; kh = [heights(d) for d in keys]
print(f"lock heights: {lh}")
print(f"key heights: {kh}")
fits = exact = 0
for l in lh:
    for k in kh:
        sums = [l[i] + k[i] for i in range(5)]
        if all(s <= 5 for s in sums): fits += 1
        if all(s == 5 for s in sums): exact += 1
print(f"part 1: {fits} lock and key pairs fit")
print(f"part 2: {exact} pairs fit exactly")

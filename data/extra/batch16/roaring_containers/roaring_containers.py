def runs(xs):
    return sum(1 for i in range(len(xs)) if i == 0 or xs[i] != xs[i - 1] + 1)

values = [3, 50, 51, 200]
values += [v for v in range(256, 512) if v % 7 != 0]
values += list(range(512, 600))
values += list(range(700, 760))
values += [1030, 1100, 1101, 1102, 1103, 1279]
chunks = {}
for v in values:
    chunks.setdefault(v >> 8, []).append(v)
total = 0
for key, xs in chunks.items():
    r = runs(xs)
    sizes = [2 * len(xs), 32, 4 * r]
    best = min(sizes)
    kind = "array" if best == sizes[0] else ("bitmap" if best == sizes[1] else "runs")
    total += best
    print(f"chunk {key}: {len(xs):>3} values, {r:>2} runs, array {sizes[0]:>3} B, bitmap 32 B, runs {sizes[2]:>3} B -> {kind}")
print(f"{len(values)} values in {total} bytes instead of {4 * len(values)}")

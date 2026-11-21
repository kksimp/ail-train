def ranges(xs):
    if len(xs) == 0:
        return "-"
    out = []
    start = xs[0]
    prev = xs[0]
    for x in xs[1:]:
        if x != prev + 1:
            out.append(f"{start}" if start == prev else f"{start}-{prev}")
            start = x
        prev = x
    out.append(f"{start}" if start == prev else f"{start}-{prev}")
    return ", ".join(out)

files = [("cart.py", [1, 2, 3, 4, 5, 6, 8, 9, 10, 12], [1, 2, 3, 8, 12]), ("tax.py", [1, 2, 4, 5], [1, 2, 4, 5]), ("api.py", [3, 4, 5, 7, 9, 10, 11, 14, 15, 16, 17], [3, 4, 9, 14]), ("util.py", [2, 3], [])]
all_lines = 0
all_hit = 0
for name, lines, hit in files:
    hit_set = set(hit)
    missed = [l for l in lines if l not in hit_set]
    n = len(lines) - len(missed)
    pct = float(n * 100) / float(len(lines))
    all_lines += len(lines)
    all_hit += n
    print(f"{name:<8} {n:>2}/{len(lines):<2} {pct:>5.1f}%  missing {ranges(missed)}")
total = float(all_hit * 100) / float(all_lines)
print(f"TOTAL    {all_hit:>2}/{all_lines:<2} {total:>5.1f}%")

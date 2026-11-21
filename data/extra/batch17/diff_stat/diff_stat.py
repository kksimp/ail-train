def scaled(n, biggest, width):
    if biggest <= width or n == 0:
        return n
    return max(n * width // biggest, 1)

files = [("src/parser.ail", 42, 17), ("src/lexer.ail", 3, 1), ("docs/guide.md", 0, 12), ("tests/parse_test.ail", 25, 0), ("README.md", 1, 1)]
biggest = max(f[1] + f[2] for f in files)
name_w = max(len(f[0]) for f in files)
adds = 0
dels = 0
for name, a, d in files:
    total = a + d
    plus = scaled(a, biggest, 20)
    minus = scaled(d, biggest, 20)
    bar = "+" * plus + "-" * minus
    print(f" {name.ljust(name_w, ' ')} | {total:>3} {bar}")
    adds += a
    dels += d
print(f" {len(files)} files changed, {adds} insertions(+), {dels} deletions(-)")

listing = ["src/main.ail 4200", "src/parse/lexer.ail 15800", "src/parse/tree.ail 9100", "docs/guide.md 2300000", "docs/img/logo.png 840000", "README.md 900"]
def human(n):
    if n >= 1048576: return f"{n // 1048576}.{n % 1048576 * 10 // 1048576}M"
    if n >= 1024: return f"{n // 1024}K"
    return f"{n}B"
tot = {}
for l in listing:
    p, s = l.split(); parts = p.split("/")
    for i in range(1, len(parts)):
        d = "/".join(parts[:i]); tot[d] = tot.get(d, 0) + int(s)
for d in sorted(tot):
    print("  " * d.count("/") + d.split("/")[-1] + "/ " + human(tot[d]))
print(f"{len(listing)} files; biggest folder: {max(tot, key=lambda d: tot[d])}")

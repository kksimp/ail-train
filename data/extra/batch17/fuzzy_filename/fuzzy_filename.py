def fuzzy(pattern, path):
    p = list(pattern.lower())
    s = list(path.lower())
    score = 0
    pi = 0
    prev = -2
    for i in range(len(s)):
        if pi < len(p) and s[i] == p[pi]:
            score += 1
            if i == prev + 1:
                score += 2
            if i == 0 or s[i - 1] in "/_-.":
                score += 3
            prev = i
            pi += 1
    return -1 if pi < len(p) else score

paths = ["src/main.ail", "src/parser/mod.ail", "docs/manual.md", "tests/main_test.ail", "src/lexer/main_loop.ail", "Makefile", "scripts/make_release.sh"]
for pat in ["main", "mk", "pmod", "tst", "zz"]:
    scored = []
    for path in paths:
        sc = fuzzy(pat, path)
        if sc >= 0:
            scored.append((sc, path))
    ranked = sorted(scored, key=lambda x: -x[0])
    shown = ", ".join(f"{x[1]} ({x[0]})" for x in ranked[:3])
    out = "no match" if len(ranked) == 0 else shown
    print(f"{pat:<5} {out}")

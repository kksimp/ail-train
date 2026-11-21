def here(re, ri, text, ti):
    if ri == len(re):
        return True
    if ri + 1 < len(re) and re[ri + 1] == '*':
        return star(re[ri], re, ri + 2, text, ti)
    if re[ri] == '$' and ri + 1 == len(re):
        return ti == len(text)
    if ti < len(text) and (re[ri] == '.' or re[ri] == text[ti]):
        return here(re, ri + 1, text, ti + 1)
    return False

def star(c, re, ri, text, ti):
    t = ti
    while True:
        if here(re, ri, text, t):
            return True
        if t < len(text) and (text[t] == c or c == '.'):
            t += 1
        else:
            return False

def matches(pattern, s):
    if len(pattern) > 0 and pattern[0] == '^':
        return here(pattern, 1, s, 0)
    for start in range(len(s) + 1):
        if here(pattern, 0, s, start):
            return True
    return False

texts = ["abc", "ac", "abbbcd", "xabcx", "cab"]
for pattern in ["ab*c", "^ab*c$", "a.c", "^c", "b*$", "x.*x"]:
    cells = []
    for t in texts:
        mark = "yes" if matches(pattern, t) else "no"
        cells.append(f"{t}={mark}")
    print(f"{pattern:<7} " + " ".join(cells))

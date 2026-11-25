import sys

SMALL = {"a", "an", "and", "as", "at", "but", "by", "for", "in", "nor", "of", "on", "or", "the", "to", "up"}

lines = sys.stdin.read().split("\n")
if lines and lines[-1] == "":
    lines.pop()


def capitalize(s):
    s = s.lower()
    return s[:1].upper() + s[1:]


def title_word(w):
    return "-".join(capitalize(p) for p in w.split("-"))


for line in lines:
    words = line.split()
    out = []
    for i, w in enumerate(words):
        edge = i == 0 or i == len(words) - 1
        if w.lower() in SMALL and not edge:
            out.append(w.lower())
        else:
            out.append(title_word(w))
    print(" ".join(out))

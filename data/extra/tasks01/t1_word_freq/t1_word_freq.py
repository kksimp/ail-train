import re
import sys

text = sys.stdin.read()
words = re.findall(r"[a-z]+", text.lower())
if not words:
    print("no words")
else:
    counts = {}
    for w in words:
        counts[w] = counts.get(w, 0) + 1
    ranked = sorted(counts.items(), key=lambda p: (-p[1], p[0]))
    for w, n in ranked[:5]:
        print(f"{w} {n}")

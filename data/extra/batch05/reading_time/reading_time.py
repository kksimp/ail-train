t = 0
for n, w in [("Intro to AIL", 820), ("Garden notes", 140), ("Deep dive: GC", 4650), ("Weekly news", 1210), ("Recipe", 455)]:
    m = (w + 229) // 230; t += m; l = "short" if m <= 2 else "medium" if m <= 8 else "long"; print(f"{n:<14} {w:>5} words  {m:>2} min  {l}")
print(f"all articles: {t} min")

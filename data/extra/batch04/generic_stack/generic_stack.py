st = [1, 2, 3, 4, 5]; r = []
while st: r.append(st.pop())
print(f"reversed: {r}")
ed = []; t = ""
for w in ["the", "quick", "brown", "fox"]: ed.append(t); t = w if t == "" else f"{t} {w}"
print(f"text: {t} ({len(ed)} undo steps)")
for _ in range(2): t = ed.pop()
print(f'after two undos: {t}; next undo gives "{ed[-1]}"')

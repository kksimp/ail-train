sub = ["maths", "art", "history", "biology"]
mk = [("Ines", [78, 92, 65, 81]), ("Jon", [88, 55, 72, 90]), ("Kim", [95, 70, 84, 77]), ("Lars", [60, 85, 91, 68])]
avg = lambda xs: sum(xs) / len(xs)
for n, s in mk: print(f"{n:<5} {avg(s):.1f}")
for i, sj in enumerate(sub):
    t = max(mk, key=lambda m: m[1][i]); print(f"{sj:<8} top: {t[0]} ({t[1][i]})")
ca = avg([x for _, s in mk for x in s])
print(f"class {ca:.2f}, above: " + ", ".join(n for n, s in mk if avg(s) > ca))

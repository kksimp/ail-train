def run(name, steps):
    print(f"{name}:")
    work = 0; idle = 0
    for i, s in enumerate(steps):
        k = s[0]
        if k == "P": d = f"preheat to {s[1]} C"; idle += s[1] // 20 * 60
        elif k == "C": d = f"chop {s[1]} ({s[2]} min)"; work += s[2] * 60
        elif k == "S": d = f"stir {s[1]} s"; work += s[1]
        elif k == "B": d = f"bake {s[1]} min"; idle += s[1] * 60
        else:
            d = "serve at once" if s[1] == 0 else f"rest {s[1]} min"; idle += s[1] * 60
        print(f"  {i + 1}. {d}")
    print(f"  hands-on {work // 60} min {work % 60} s, waiting {idle // 60} min {idle % 60} s")
run("root bake", [("P", 200), ("C", "onions", 6), ("C", "carrots", 4), ("S", 90), ("B", 35), ("R", 10)])
run("quick eggs", [("S", 45), ("R", 0)])

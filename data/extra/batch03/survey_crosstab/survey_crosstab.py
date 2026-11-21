ans = [("18-29", "yes"), ("30-49", "no"), ("18-29", "yes"), ("50+", "no"), ("30-49", "yes"), ("50+", "no"), ("18-29", "no"), ("30-49", "yes"), ("50+", "yes"), ("18-29", "yes"), ("30-49", "unsure"), ("50+", "no")]
bs = ["18-29", "30-49", "50+"]; cs = ["yes", "no", "unsure"]
c = {}
for a in ans: c[a] = c.get(a, 0) + 1
print(f"{'band':<7}" + "".join(f"{x:>8}" for x in cs))
for b in bs:
    t = sum(c.get((b, x), 0) for x in cs)
    print(f"{b:<7}" + "".join(f"{c.get((b, x), 0):>3} {(c.get((b, x), 0) * 200 + t) // (t * 2):>3}%" for x in cs))

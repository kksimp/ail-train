import math
tr = [("spam", "win cash now"), ("spam", "cheap cash offer now"), ("spam", "win a free prize now"), ("ham", "lunch at noon"), ("ham", "project meeting moved to noon"), ("ham", "can you send the project notes"), ("ham", "free for lunch tomorrow")]
sp = {}; hm = {}; st = ht = 0; sm = 0; voc = set()
for lab, txt in tr:
    for w in txt.split():
        voc.add(w)
        if lab == "spam": sp[w] = sp.get(w, 0) + 1; st += 1
        else: hm[w] = hm.get(w, 0) + 1; ht += 1
    if lab == "spam": sm += 1
pr = sm / len(tr)
def score(ws, c, tot, prior):
    s = math.log(prior)
    for w in ws: s += math.log((c.get(w, 0) + 1) / (tot + len(voc)))
    return s
for m in ["free cash prize", "project lunch at noon", "win the meeting", "send cash now"]:
    a = score(m.split(), sp, st, pr); b = score(m.split(), hm, ht, 1.0 - pr)
    print(f"{m:<22} log odds {a - b:>6.2f} -> {'spam' if a > b else 'ham'}")

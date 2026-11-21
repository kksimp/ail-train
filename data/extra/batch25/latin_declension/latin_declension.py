def classify(nom, gen):
    if nom.endswith("a") and gen.endswith("ae"):
        return "Decl.First"
    if nom.endswith("us") and gen.endswith("ī"):
        return "Decl.SecondMasc"
    if nom.endswith("um") and gen.endswith("ī"):
        return "Decl.SecondNeut"
    return None

def forms(nom, d):
    if d == "Decl.First":
        return [nom[:len(nom) - 1] + e for e in ["a", "ae", "ae", "am", "ā", "ae", "ārum", "īs", "ās", "īs"]]
    if d == "Decl.SecondMasc":
        return [nom[:len(nom) - 2] + e for e in ["us", "ī", "ō", "um", "ō", "ī", "ōrum", "īs", "ōs", "īs"]]
    return [nom[:len(nom) - 2] + e for e in ["um", "ī", "ō", "um", "ō", "a", "ōrum", "īs", "a", "īs"]]

nouns = [("puella", "puellae"), ("dominus", "dominī"), ("bellum", "bellī"), ("rēx", "rēgis"), ("via", "viae")]
for nom, gen in nouns:
    d = classify(nom, gen)
    if d is not None:
        fs = forms(nom, d)
        sg = " ".join(fs[:5])
        pl = " ".join(fs[5:])
        counts = {}
        for f in fs:
            counts[f] = counts.get(f, 0) + 1
        most = sorted(counts.keys(), key=lambda k: -counts[k])[0]
        print(f"{nom} ({d}): sg {sg} | pl {pl} | {most} x{counts[most]}")
    else:
        print(f"skipped {nom}, {gen}: not first or second declension")

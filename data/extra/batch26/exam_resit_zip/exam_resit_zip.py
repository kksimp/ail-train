names = ["Ada", "Bo", "Cy", "Di", "Ed"]
first = [48, 71, 39, 55, 62]; resit = [61, 0, 44, 52, 0]
pairs = list(zip(first, resit))
for i, (a, b) in enumerate(pairs):
    mark = max(a, b)
    verdict = "pass" if mark >= 50 else "fail"
    note = "no resit" if b == 0 else (f"resit +{b - a}" if b > a else f"resit lower, kept {a}")
    print(f"{names[i]:<4} {a:>3} {b:>3} -> {mark:>3} {verdict} ({note})")
passed = sum(1 for a, b in pairs if max(a, b) >= 50)
sat = sum(1 for a, b in pairs if b > 0)
gained = sum(1 for a, b in pairs if b > a)
print(f"passed {passed} of {len(names)}; {gained} of {sat} resits improved")

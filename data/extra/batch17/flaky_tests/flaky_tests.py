runs = [{"login": "P", "checkout": "P", "search": "F", "export": "P", "upload": "F"}, {"login": "P", "checkout": "F", "search": "F", "export": "P", "upload": "F"}, {"login": "P", "checkout": "P", "search": "F", "export": "F", "upload": "F"}, {"login": "P", "checkout": "P", "search": "F", "export": "P", "upload": "F"}, {"login": "P", "checkout": "F", "search": "F", "export": "P"}]
history = {}
for r in runs:
    for test, result in r.items():
        history.setdefault(test, []).append(result)
flaky = 0
for test, results in history.items():
    passes = len([x for x in results if x == "P"])
    rate = passes * 100 // len(results)
    kind = "stable" if passes == len(results) else "broken" if passes == 0 else "FLAKY"
    line = "".join(results)
    fails = [i + 1 for i, x in enumerate(results) if x == "F"]
    note = f" failed in runs {fails}" if kind == "FLAKY" else ""
    if kind == "FLAKY":
        flaky += 1
    print(f"{test:<9} {line:<6} {rate:>3}% {kind}{note}")
print(f"{flaky} flaky tests over {len(runs)} runs")

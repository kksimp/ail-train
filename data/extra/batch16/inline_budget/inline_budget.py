size = {"main": 20, "parse": 14, "square": 3, "log_line": 9, "fact": 6, "render": 40}
calls = [("main", "parse"), ("main", "square"), ("main", "render"), ("parse", "square"), ("parse", "log_line"), ("main", "log_line"), ("main", "fact"), ("fact", "fact"), ("render", "square")]
recursive = set(c for a, c in calls if a == c)
original = dict(size)
budget = 25
growth = 0
order = sorted(calls, key=lambda s: original[s[1]])
for caller, callee in order:
    body = size[callee]
    if callee in recursive:
        print(f"{caller} -> {callee}: kept (recursive)")
    elif body > 15:
        print(f"{caller} -> {callee}: kept (body {body} too big)")
    elif growth + body - 1 > budget:
        print(f"{caller} -> {callee}: kept (budget, growth would be {growth + body - 1})")
    else:
        growth += body - 1
        size[caller] += body - 1
        print(f"{caller} -> {callee}: inlined, growth {growth}")
for f, n in size.items():
    print(f"{f:<9} {original[f]:>2} -> {n:>2}")

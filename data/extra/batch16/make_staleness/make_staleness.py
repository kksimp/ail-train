def build(t, rules, mtime, clock, seen):
    if t in seen:
        return
    seen.add(t)
    deps = rules.get(t, [])
    for d in deps:
        if d in rules:
            build(d, rules, mtime, clock, seen)
    mine = mtime.get(t, -1)
    why = ""
    if mine < 0:
        why = "missing"
    else:
        for d in deps:
            if why == "" and mtime.get(d, 0) > mine:
                why = f"{d} is newer"
    if why == "":
        return
    clock[0] += 1
    mtime[t] = clock[0]
    print(f"  rebuild {t:<7} ({why})")

def run(name, rules, mtime, clock):
    print(f"{name}:")
    seen = set()
    before = clock[0]
    for t in ["app", "docs"]:
        build(t, rules, mtime, clock, seen)
    if clock[0] == before:
        print("  nothing to do")

rules = {"app": ["main.o", "util.o"], "main.o": ["main.c", "util.h"], "util.o": ["util.c", "util.h"], "docs": ["readme.md"]}
mtime = {"main.c": 10, "util.c": 5, "util.h": 12, "main.o": 11, "util.o": 13, "app": 14, "readme.md": 3}
clock = [20]
run("first make", rules, mtime, clock)
run("second make", rules, mtime, clock)
mtime["util.c"] = 30
clock[0] = 30
run("after editing util.c", rules, mtime, clock)

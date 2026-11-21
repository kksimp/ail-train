def parse(argv):
    known = {"name": True, "count": True, "o": True, "v": False, "x": False, "verbose": False}
    flags = {}
    positional = []
    i = 0
    while i < len(argv):
        a = argv[i]
        i += 1
        if a == "--":
            positional.extend(argv[i:])
            break
        if not a.startswith("-") or a == "-":
            positional.append(a)
            continue
        body = a[2:] if a.startswith("--") else a[1:]
        eq = body.find("=")
        name = body[:eq] if eq >= 0 else body
        if name not in known:
            return None, f"unknown flag {a}"
        if not known[name]:
            flags[name] = "true"
        elif eq >= 0:
            flags[name] = body[eq + 1:]
        elif i < len(argv):
            flags[name] = argv[i]
            i += 1
        else:
            return None, f"{a} needs a value"
    return (flags, positional), None

cmds = [["--name=Ann", "-v", "report.txt"], ["-x", "--count", "3", "a.txt", "b.txt"], ["-o", "out.txt", "--", "-strange-file"], ["--count"], ["-z"], ["--verbose", "-", "--name", "Bo Li"]]
for argv in cmds:
    line = " ".join(argv)
    p, err = parse(argv)
    if p is not None:
        shown_flags = ",".join(f"{k}={v}" for k, v in p[0].items())
        shown_args = ",".join(p[1])
        print(f"{line:<30} flags [{shown_flags}] args [{shown_args}]")
    else:
        print(f"{line:<30} error: {err}")

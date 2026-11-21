def merge(base, ours, theirs):
    out = []
    for i in range(len(base)):
        o = ours[i]
        t = theirs[i]
        if o == t:
            out.append(o)
        elif o == base[i]:
            out.append(t)
        elif t == base[i]:
            out.append(o)
        else:
            out += ["<<<<<<< ours", o, "=======", t, ">>>>>>> theirs"]
    return [l for l in out if l != ""]

base = ["host = localhost", "port = 8080", "workers = 4", "debug = false", "log = info", "timeout = 30"]
ours = ["host = localhost", "port = 9090", "workers = 4", "debug = true", "", "timeout = 60"]
theirs = ["host = 0.0.0.0", "port = 8080", "workers = 8", "debug = true", "", "timeout = 45"]
merged = merge(base, ours, theirs)
for line in merged:
    print(line)
conflicts = sum(1 for l in merged if l.startswith("<<<<"))
print(f"{conflicts} conflict(s) in {len(base)} lines")

def parse(s):
    return tuple(int(x) for x in s.split("."))

def upper(v, op):
    if op == "~" or v[0] == 0:
        return (v[0], v[1] + 1, 0)
    return (v[0] + 1, 0, 0)

def satisfies(v, rng):
    if rng.startswith(">="):
        return v >= parse(rng[2:])
    if rng.startswith("^") or rng.startswith("~"):
        low = parse(rng[1:])
        high = upper(low, rng[0:1])
        return low <= v < high
    return v == parse(rng)

versions = ["0.9.4", "1.0.0", "1.2.3", "1.2.9", "1.3.0", "1.10.1", "2.0.0", "0.2.5", "0.3.0"]
for rng in ["^1.2.3", "~1.2.3", "^0.2.1", ">=1.3.0", "1.2.9"]:
    hits = [s for s in versions if satisfies(parse(s), rng)]
    shown = "none" if not hits else " ".join(hits)
    print(f"{rng:<8} {shown}")
newest = max(parse(s) for s in versions)
print(f"newest: {newest[0]}.{newest[1]}.{newest[2]}")

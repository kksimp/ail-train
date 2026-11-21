def parse_layer(text):
    body = text.split(": ")[1]
    return [[int(w) for w in part.split(" ")] for part in body.split("; ")]

def map_one(rules, v):
    for r in rules:
        if r[1] <= v < r[1] + r[2]:
            return v - r[1] + r[0]
    return v

def map_spans(rules, spans):
    pending = spans; done = []
    for r in rules:
        rest = []
        for s in pending:
            lo = max(s[0], r[1]); hi = min(s[1], r[1] + r[2])
            if lo < hi:
                done.append([lo - r[1] + r[0], hi - r[1] + r[0]])
                if s[0] < lo: rest.append([s[0], lo])
                if hi < s[1]: rest.append([hi, s[1]])
            else:
                rest.append(s)
        pending = rest
    done.extend(pending)
    return done

seeds = [12, 30, 55, 8, 71, 14]
layers = [parse_layer(t) for t in ["soil: 40 10 15; 10 30 20; 70 55 10", "water: 0 40 12; 60 0 10", "light: 25 60 30; 5 85 10"]]
low = 1000000
for s in seeds:
    v = s
    for rules in layers:
        v = map_one(rules, v)
    print(f"seed {s} ends on plot {v}")
    low = min(low, v)
print(f"part 1: lowest plot {low}")
spans = [[12, 42], [55, 63], [71, 85]]
for rules in layers:
    spans = map_spans(rules, spans)
print(f"part 2: {len(spans)} ranges after the light layer, lowest plot {min(s[0] for s in spans)}")

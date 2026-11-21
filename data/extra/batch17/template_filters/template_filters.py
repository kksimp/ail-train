def title_case(s):
    return " ".join(w[:1].upper() + w[1:].lower() for w in s.split(" "))

def money(v):
    try:
        c = int(v)
    except ValueError:
        c = 0
    return f"{c // 100}.{c % 100:02}"

def apply(v, f):
    parts = f.split(":")
    name = parts[0]
    arg = parts[1] if len(parts) > 1 else ""
    n = int(arg) if arg.isdigit() else 0
    if name == "upper":
        return v.upper()
    if name == "title":
        return title_case(v)
    if name == "pad":
        return v.ljust(n, '.')
    if name == "default":
        return arg if v == "" else v
    if name == "money":
        return money(v)
    if name == "cut":
        return v[:n] + "..." if len(v) > n else v
    return f"[no filter {name}]"

def fill(t, vars):
    out = []
    rest = t
    while True:
        at = rest.find("{{")
        if at < 0:
            break
        out.append(rest[:at])
        after = rest[at + 2:]
        close = after.find("}}")
        if close < 0:
            close = len(after)
        steps = [p.strip() for p in after[:close].split("|")]
        v = vars.get(steps[0], "")
        for f in steps[1:]:
            v = apply(v, f)
        out.append(v)
        rest = after[min(close + 2, len(after)):]
    out.append(rest)
    return "".join(out)

t = "{{ name | title | pad:14 }} {{ plan | upper }} {{ due | money }} {{ note | default:none | cut:12 }}"
rows = [{"name": "ada lovelace", "plan": "pro", "due": "4250", "note": ""}, {"name": "ALAN turing", "plan": "basic", "due": "999", "note": "pays by card each month"}, {"name": "grace", "plan": "team", "due": "120000", "note": "vip"}]
for r in rows:
    print(fill(t, r))
print(fill("{{ plan | shout }}!", {"plan": "pro"}))

class FieldRule:
    def __init__(self, name, kind, required, lo, hi, choices):
        self.name, self.kind, self.required, self.lo, self.hi, self.choices = name, kind, required, lo, hi, choices

def to_int(s):
    t = s[1:] if s.startswith("-") else s
    return int(s) if t.isdigit() and t != "" else None

def problems(rec, schema):
    out = []
    for f in schema:
        raw = rec.get(f.name, "")
        if raw == "":
            if f.required:
                out.append(f"{f.name}: missing")
            continue
        if f.kind == "int":
            n = to_int(raw)
            if n is not None:
                if n < f.lo or n > f.hi:
                    out.append(f"{f.name}: {n} outside {f.lo}..{f.hi}")
            else:
                out.append(f"{f.name}: '{raw}' is not a number")
        elif f.kind == "choice" and raw not in f.choices:
            shown = "/".join(f.choices)
            out.append(f"{f.name}: '{raw}' not one of {shown}")
    for k, v in rec.items():
        if not any(f.name == k for f in schema):
            out.append(f"{k}: unknown field")
    return out

schema = [FieldRule("id", "int", True, 1, 99999, []), FieldRule("name", "text", True, 0, 0, []), FieldRule("age", "int", False, 0, 130, []), FieldRule("plan", "choice", True, 0, 0, ["free", "pro", "team"])]
records = [{"id": "17", "name": "Ana", "age": "34", "plan": "pro"}, {"id": "x9", "name": "", "plan": "gold"}, {"id": "120000", "name": "Ben", "age": "200", "plan": "free", "nick": "b"}, {"id": "5", "name": "Cy", "plan": "team"}]
bad = 0
for i, r in enumerate(records):
    ps = problems(r, schema)
    if len(ps) == 0:
        print(f"record {i + 1}: valid")
    else:
        bad += 1
        print(f"record {i + 1}: {len(ps)} problem(s)")
        for p in ps:
            print(f"    {p}")
print(f"{len(records) - bad} valid, {bad} invalid")

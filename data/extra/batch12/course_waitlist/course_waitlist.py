courses = {"ML": {"cap": 2, "needs": ["Stats", "Python"], "seats": [], "queue": []}, "Art": {"cap": 3, "needs": [], "seats": [], "queue": []}}
passed = {"ann": ["Stats", "Python"], "bo": ["Python"], "cy": ["Stats", "Python"], "di": ["Stats", "Python", "Art"]}
asks = [("ann", "ML"), ("bo", "ML"), ("cy", "ML"), ("di", "ML"), ("bo", "Art")]

def enrol(c, who):
    if len(c["seats"]) < c["cap"]:
        c["seats"].append(who)
        return "enrolled"
    c["queue"].append(who)
    return f"waitlisted at {len(c['queue'])}"

def drop(c, who):
    if who not in c["seats"]:
        return "not enrolled"
    c["seats"].remove(who)
    if c["queue"]:
        nxt = c["queue"].pop(0)
        c["seats"].append(nxt)
        return f"{nxt} moves up"
    return "seat left empty"

def check(has, needs):
    for n in needs:
        if n not in has:
            return None, f"needs {n}"
    return len(needs), None

import json
def show(xs):
    return json.dumps(xs)

for who, name in asks:
    has = passed.get(who, [])
    met, err = check(has, courses[name]["needs"])
    if err is not None:
        print(f"{who} -> {name}: refused, {err}")
        continue
    result = enrol(courses[name], who)
    print(f"{who} -> {name}: {result} ({met} prerequisites met)")
print(f"ann drops ML: {drop(courses['ML'], 'ann')}")
for name, c in courses.items():
    print(f"{name}: seats {show(c['seats'])}, waiting {show(c['queue'])}")

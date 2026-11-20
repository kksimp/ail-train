users = [("ann", None, 41), ("bob", "ann", None), ("cy", "bob", 29)]

def manager_of(name):
    for n, m, _ in users:
        if n == name:
            return m or "(none)"
    return "(no such user)"

for name in ["ann", "bob", "cy", "dan"]:
    print(f"{name}: manager {manager_of(name)}")
for n, _, age in users:
    known = "unknown" if age is None else "known"
    print(f"{n} age {known}, next year {(age or 0) + 1}")
print(3)
print(0)
print("cy reports to bob")
print(2)

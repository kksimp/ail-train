def classify(spec):
    if "==" in spec:
        return "Exact"
    if "~=" in spec:
        return "Compatible"
    if ">" in spec or "<" in spec:
        return "Ranged"
    return "Loose"

def package_name(spec):
    end = len(spec)
    for i, c in enumerate(spec):
        if not (c.isalnum() or c in "-_."):
            end = i
            break
    return spec[:end].lower()

lines = ["# web", "requests==2.31.0", "Flask>=2.0,<3", "numpy", "django~=4.2", "", "pytest==7.4.0 ; python_version > '3.8'", "-r dev.txt", "black", "SQLAlchemy==2.0.20  # pinned for prod"]
groups = {}
for raw in lines:
    line = raw.split("#")[0].split(";")[0].strip()
    if line == "" or line.startswith("-"):
        continue
    groups.setdefault(classify(line), []).append(package_name(line))
for k in ["Exact", "Compatible", "Ranged", "Loose"]:
    names = groups.get(k, [])
    print(f"{k:<10} {len(names)}  {' '.join(names)}".rstrip())
loose = len(groups.get("Loose", []))
total = sum(len(v) for v in groups.values())
print(f"{total - loose} of {total} packages have a version constraint")

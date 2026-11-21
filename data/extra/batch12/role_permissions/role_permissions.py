grants = {"viewer": ["read"], "editor": ["write", "comment"], "auditor": ["export", "read_logs"], "admin": ["delete", "invite"]}
parents = {"editor": ["viewer"], "admin": ["editor", "auditor"]}
users = {"rae": ["viewer"], "sol": ["editor"], "tam": ["auditor", "viewer"], "uma": ["admin"]}

def actions(role, seen):
    out = set()
    if role in seen:
        return out
    seen.add(role)
    for a in grants.get(role, []):
        out.add(a)
    for p in parents.get(role, []):
        out |= actions(p, seen)
    return out

def can(roles, action):
    seen = set()
    for r in roles:
        if action in actions(r, seen):
            return True
    return False

checks = ["read", "write", "export", "delete"]
header = "".join(f"{c:<8}" for c in checks).rstrip()
print(f"user  {header}")
for name, roles in users.items():
    cells = "".join("yes     " if can(roles, c) else "-       " for c in checks).rstrip()
    print(f"{name:<5} {cells}")
print(f"admin can: {' '.join(sorted(actions('admin', set())))}")

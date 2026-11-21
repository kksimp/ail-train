class Commit:
    def __init__(self, kind, scope, text, breaking):
        self.kind, self.scope, self.text, self.breaking = kind, scope, text, breaking

def parse(msg):
    colon = msg.find(": ")
    if colon < 0:
        return None
    head = msg[:colon]
    breaking = head.endswith("!") or "BREAKING" in msg
    if head.endswith("!"):
        head = head[:-1]
    scope = ""
    o = head.find("(")
    if o >= 0:
        scope = head[o + 1:len(head) - 1]
        head = head[:o]
    return Commit(head, scope, msg[colon + 2:], breaking)

log = ["feat(api): add search endpoint", "fix: crash on empty cart", "docs: explain config file", "fix(ui): button overlaps footer", "refactor!: drop the v1 payment flow", "updated stuff", "feat: export orders as CSV", "chore(deps): bump parser"]
version = [1, 4, 2]
sections = [("feat", "Features"), ("fix", "Bug fixes"), ("docs", "Documentation")]
commits = [c for c in (parse(m) for m in log) if c is not None]
print(f"{len(log) - len(commits)} commit(s) not in the convention")
for kind, title in sections:
    items = [c for c in commits if c.kind == kind]
    if len(items) > 0:
        print(f"## {title}")
        for c in items:
            where = "" if c.scope == "" else f"**{c.scope}:** "
            print(f"- {where}{c.text}")
breaking = [c for c in commits if c.breaking]
if len(breaking) > 0:
    print("## Breaking changes")
    for c in breaking:
        print(f"- {c.text}")
major = len(breaking) > 0
minor = any(c.kind == "feat" for c in commits)
nxt = [version[0] + 1, 0, 0] if major else [version[0], version[1] + 1, 0] if minor else [version[0], version[1], version[2] + 1]
print(f"version {version[0]}.{version[1]}.{version[2]} -> {nxt[0]}.{nxt[1]}.{nxt[2]}")

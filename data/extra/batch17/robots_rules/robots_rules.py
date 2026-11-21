class Rule:
    def __init__(self, agent, allow, prefix):
        self.agent, self.allow, self.prefix = agent, allow, prefix

def parse(text):
    rules = []
    agents = []
    in_rules = False
    for raw in text.split("\n"):
        line = raw.split("#")[0].strip()
        colon = line.find(":")
        if colon < 0:
            continue
        key = line[:colon].strip().lower()
        val = line[colon + 1:].strip()
        if key == "user-agent":
            if in_rules:
                agents = []
                in_rules = False
            agents.append(val.lower())
        elif key == "allow" or key == "disallow":
            in_rules = True
            for a in agents:
                rules.append(Rule(a, key == "allow", val))
    return rules

def allowed(rules, bot, path):
    mine = [r for r in rules if r.agent == bot]
    group = [r for r in rules if r.agent == "*"] if len(mine) == 0 else mine
    best = -1
    verdict = True
    for r in group:
        if r.prefix == "" or not path.startswith(r.prefix):
            continue
        if len(r.prefix) > best or (len(r.prefix) == best and r.allow):
            best = len(r.prefix)
            verdict = r.allow
    return verdict

text = "User-agent: *\nDisallow: /private/\nAllow: /private/press/\nDisallow: /tmp\n\n# news crawler\nUser-agent: newsbot\nDisallow: /\nAllow: /news/\n\nUser-agent: archiver\nUser-agent: oldbot\nDisallow:"
rules = parse(text)
print(f"{len(rules)} rules")
checks = [("crawler", "/index.html"), ("crawler", "/private/plans.pdf"), ("crawler", "/private/press/launch.html"), ("crawler", "/tmp2/x"), ("newsbot", "/news/today"), ("newsbot", "/about"), ("archiver", "/private/plans.pdf")]
for bot, path in checks:
    word = "allow" if allowed(rules, bot, path) else "block"
    print(f"{bot:<9} {path:<28} {word}")

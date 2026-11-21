def lint(msg):
    lines = msg.split("\n")
    subject = lines[0]
    out = []
    if len(subject) > 50:
        out.append(f"subject is {len(subject)} chars (max 50)")
    first = subject[0] if subject else 'a'
    if not first.isupper():
        out.append("subject should start with a capital")
    if subject.endswith("."):
        out.append("subject ends with a full stop")
    ws = subject.split()
    verb = (ws[0] if ws else "").lower()
    if verb.endswith("ed") or verb.endswith("ing"):
        out.append(f"use the imperative: '{verb}'")
    if len(lines) > 1 and lines[1] != "":
        out.append("line 2 must be blank")
    for i, l in enumerate(lines):
        if i >= 2 and len(l) > 72:
            out.append(f"body line {i + 1} is {len(l)} chars (max 72)")
    return out

msgs = ["Add retry to the upload client", "fixed the login bug.", "Adding a much longer subject line that keeps going past fifty", "Update parser\nAlso handles tabs now", "Remove dead code\n\nThe old exporter has not been called since the reporting rewrite last spring and only slows the build."]
clean = 0
for i, m in enumerate(msgs):
    problems = lint(m)
    title = m.split("\n")[0]
    if len(problems) == 0:
        clean += 1
        print(f"#{i + 1} ok: {title}")
    else:
        print(f"#{i + 1} {len(problems)} problem(s): {title}")
        for p in problems:
            print(f"    {p}")
print(f"{clean} of {len(msgs)} messages pass")

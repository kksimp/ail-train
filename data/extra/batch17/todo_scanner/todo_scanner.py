class Note:
    def __init__(self, file, line, tag, owner, text):
        self.file, self.line, self.tag, self.owner, self.text = file, line, tag, owner, text

def scan(file, lines):
    out = []
    for i, l in enumerate(lines):
        at = l.find("#")
        if at < 0:
            continue
        comment = l[at + 1:].strip()
        for tag in ["TODO", "FIXME", "XXX"]:
            if comment.startswith(tag):
                rest = comment[len(tag):]
                owner = "nobody"
                body = rest
                if body.startswith("("):
                    close = body.find(")")
                    owner = body[1:close]
                    body = body[close + 1:]
                text = (body[1:] if body.startswith(":") else body).strip()
                out.append(Note(file, i + 1, tag, owner, text))
    return out

def if_rank(tag):
    return 0 if tag == "FIXME" else 1

notes = []
notes.extend(scan("cart.py", ["total = 0  # TODO(ana): use Decimal", "# FIXME(ben): rounding is wrong for refunds", "x = 1", "# TODO handle empty basket"]))
notes.extend(scan("api.py", ["# XXX: temporary hack", "def get():  # TODO(ana): add caching", "    pass  # FIXME: crashes on None"]))
notes.extend(scan("ui.py", ["# a normal comment", "# TODO(cy): dark mode"]))
ordered = sorted(notes, key=lambda n: (n.owner, if_rank(n.tag), n.file, n.line))
current = ""
for n in ordered:
    if n.owner != current:
        print(f"{n.owner}:")
        current = n.owner
    print(f"  {n.tag:<5} {n.file}:{n.line} {n.text}")
per_file = {}
for n in notes:
    per_file[n.file] = per_file.get(n.file, 0) + 1
busiest = sorted(per_file.keys(), key=lambda f: -per_file[f])
print(f"most notes: {busiest[0]} ({per_file[busiest[0]]})")

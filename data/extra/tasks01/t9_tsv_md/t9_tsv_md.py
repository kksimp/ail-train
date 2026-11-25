import sys

lines = [l for l in sys.stdin.read().split("\n") if l != ""]
if lines:
    head = [c.strip() for c in lines[0].split("\t")]
    n = len(head)
    aligns = []
    names = []
    for h in head:
        if h.startswith(">"):
            aligns.append("---:")
            h = h[1:].strip()
        elif h.startswith("^"):
            aligns.append(":---:")
            h = h[1:].strip()
        else:
            aligns.append("---")
        names.append(h)
    def row(cells):
        return "| " + " | ".join(c.replace("|", "\|") for c in cells) + " |"
    print(row(names))
    print("| " + " | ".join(aligns) + " |")
    for l in lines[1:]:
        cells = [c.strip() for c in l.split("\t")][:n]
        cells += [""] * (n - len(cells))
        print(row(cells))

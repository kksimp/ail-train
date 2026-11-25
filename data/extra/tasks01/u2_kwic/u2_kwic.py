import sys

PUNCT = ".,;:!?\"'()"

def norm(t):
    return t.lower().strip(PUNCT)

def main():
    lines = sys.stdin.read().splitlines()
    if len(lines) < 2:
        print("bad input")
        return
    key = norm(lines[0].strip())
    if key == "":
        print("bad input")
        return
    ws = lines[1].strip()
    if not ws.isdigit():
        print("bad width")
        return
    w = int(ws)
    toks = []
    for ln in lines[2:]:
        toks.extend(ln.split())
    hits = 0
    for i, t in enumerate(toks):
        if norm(t) == key:
            hits += 1
            parts = toks[max(0, i - w):i] + ["[" + t + "]"] + toks[i + 1:i + 1 + w]
            print(f"{i + 1}: " + " ".join(parts))
    if hits == 0:
        print("no matches")
    else:
        print(f"matches={hits}")

main()

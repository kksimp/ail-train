import sys

def main():
    text = sys.stdin.read()
    pieces = []
    cur = []
    for ch in text:
        if ch in ".!?":
            pieces.append("".join(cur))
            cur = []
        else:
            cur.append(ch)
    pieces.append("".join(cur))
    sents = []
    for p in pieces:
        ws = p.split()
        if ws:
            sents.append(ws)
    if not sents:
        print("no sentences")
        return
    total = 0
    longest = 0
    for i, ws in enumerate(sents, 1):
        c = len(" ".join(ws))
        print(f"{i}: {len(ws)} words, {c} chars")
        total += len(ws)
        longest = max(longest, len(ws))
    print(f"sentences={len(sents)} words={total} longest={longest}")

main()

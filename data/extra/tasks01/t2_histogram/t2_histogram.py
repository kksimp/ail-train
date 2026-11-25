import re, sys

def main():
    text = sys.stdin.read()
    lines = text.split("\n")
    first = lines[0].strip() if lines else ""
    if not re.fullmatch(r"[0-9]+", first) or int(first) <= 0:
        print("error: bad width")
        return
    w = int(first)
    counts = {}
    invalid = 0
    total = 0
    for tok in "\n".join(lines[1:]).split():
        if re.fullmatch(r"-?[0-9]+", tok):
            b = int(tok) // w
            counts[b] = counts.get(b, 0) + 1
            total += 1
        else:
            invalid += 1
    if counts:
        for b in range(min(counts), max(counts) + 1):
            c = counts.get(b, 0)
            head = f"[{b * w}..{b * w + w - 1}] {c}"
            print(head + (" " + "#" * c if c else ""))
    print(f"total {total} invalid {invalid}")

main()

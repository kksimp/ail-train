import sys

def main():
    lines = sys.stdin.read().splitlines()
    flagged = 0
    for i, ln in enumerate(lines, 1):
        stripped = ln.rstrip(" \t")
        tail = ln[len(stripped):]
        if not tail:
            continue
        flagged += 1
        if set(tail) == {" "}:
            kind = "spaces"
        elif set(tail) == {"\t"}:
            kind = "tabs"
        else:
            kind = "mixed"
        suffix = " (blank)" if stripped == "" else ""
        print(f"{i}: {len(tail)} {kind}{suffix}")
    if flagged == 0:
        print("clean")
    else:
        print(f"flagged={flagged} of {len(lines)} lines")

main()

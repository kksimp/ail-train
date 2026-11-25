import sys

PAIR = {")": "(", "]": "[", "}": "{"}
text = sys.stdin.read()
lines = text.splitlines()
for line in lines:
    stack = []
    res = None
    for i, c in enumerate(line, 1):
        if c in "([{":
            stack.append((c, i))
        elif c in PAIR:
            if not stack:
                res = f"unmatched {c} at {i}"
                break
            o, oc = stack[-1]
            if o != PAIR[c]:
                res = f"mismatch at {i}: found {c} but {o} from {oc} is open"
                break
            stack.pop()
    if res is None:
        if stack:
            o, oc = stack[-1]
            res = f"unclosed {o} at {oc}"
        else:
            res = "ok"
    print(res)

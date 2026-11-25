import sys


def digits(s):
    return s != "" and all("0" <= c <= "9" for c in s)


def alnum(s):
    return s != "" and all(("0" <= c <= "9") or ("a" <= c <= "z") or ("A" <= c <= "Z") for c in s)


def key(t):
    core, dash, pre = t.partition("-")
    parts = core.split(".")
    if len(parts) != 3:
        return None
    for p in parts:
        if not digits(p) or len(p) > 9:
            return None
    ids = []
    if dash:
        for ident in pre.split("."):
            if not alnum(ident):
                return None
            ids.append((0, int(ident), "") if digits(ident) else (1, 0, ident))
    nums = tuple(int(p) for p in parts)
    return nums + (0 if dash else 1, ids)


valid, bad = [], []
for line in sys.stdin.read().split("\n"):
    t = line.strip(" ")
    if t == "":
        continue
    k = key(t)
    if k is None:
        bad.append(t)
    else:
        valid.append((k, t))
valid.sort(key=lambda kt: kt[0])
for _, t in valid:
    print(t)
for t in bad:
    print("invalid: " + t)

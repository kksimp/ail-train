import sys


def shape(s, pat):
    if len(s) != len(pat):
        return False
    for c, p in zip(s, pat):
        if p == "d":
            if not ("0" <= c <= "9"):
                return False
        elif c != p:
            return False
    return True


counts = {"ERROR": 0, "WARN": 0, "INFO": 0, "DEBUG": 0}
malformed = 0
first = last = None
first_err = None
for line in sys.stdin.read().split("\n"):
    t = line.strip(" ")
    if t == "":
        continue
    parts = t.split(" ", 3)
    if len(parts) < 3 or not shape(parts[0], "dddd-dd-dd") or not shape(parts[1], "dd:dd:dd") or parts[2] not in counts:
        malformed += 1
        continue
    counts[parts[2]] += 1
    stamp = parts[0] + " " + parts[1]
    if first is None:
        first = stamp
    last = stamp
    if parts[2] == "ERROR" and first_err is None:
        msg = parts[3].strip(" ") if len(parts) == 4 else ""
        first_err = msg if msg != "" else "(no message)"
for k in ("ERROR", "WARN", "INFO", "DEBUG"):
    print(f"{k} {counts[k]}")
print(f"malformed {malformed}")
if first is not None:
    print(f"span {first} .. {last}")
if first_err is not None:
    print(f"first error: {first_err}")

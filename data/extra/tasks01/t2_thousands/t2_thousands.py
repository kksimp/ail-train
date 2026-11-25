import re, sys

def add_sep(num, sep):
    neg = num.startswith("-")
    digits = (num[1:] if neg else num).lstrip("0") or "0"
    neg = neg and digits != "0"
    groups = []
    while len(digits) > 3:
        groups.append(digits[-3:])
        digits = digits[:-3]
    groups.append(digits)
    return ("-" if neg else "") + sep.join(reversed(groups))

def strip_sep(num, sep):
    neg = num.startswith("-")
    body = num[1:] if neg else num
    parts = body.split(sep)
    first = parts[0]
    if not re.fullmatch(r"[0-9]{1,3}", first):
        return None
    if first.startswith("0") and (first != "0" or len(parts) > 1):
        return None
    for p in parts[1:]:
        if not re.fullmatch(r"[0-9]{3}", p):
            return None
    return ("-" if neg else "") + "".join(parts)

def main():
    lines = sys.stdin.read().split("\n")
    if lines[-1] == "":
        lines.pop()
    ok = err = 0
    for k, raw in enumerate(lines, 1):
        f = raw.split(" ")
        f = [x for x in f if x != ""]
        if not f:
            continue
        if len(f) != 3 or f[0] not in ("add", "strip") or len(f[1]) != 1 or f[1] in "0123456789- ":
            print(f"line {k}: bad command")
            err += 1
            continue
        cmd, sep, num = f
        if cmd == "add":
            res = add_sep(num, sep) if re.fullmatch(r"-?[0-9]{1,18}", num) else None
        else:
            res = strip_sep(num, sep)
        if res is None:
            print(f"line {k}: bad number")
            err += 1
        else:
            print(res)
            ok += 1
    print(f"done {ok} errors {err}")

main()

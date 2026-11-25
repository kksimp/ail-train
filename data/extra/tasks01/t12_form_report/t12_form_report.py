import sys

FIELDS = ["name", "age", "email", "zip"]


def all_digits(s):
    return all("0" <= c <= "9" for c in s)


def email_ok(s):
    if " " in s or s.count("@") != 1:
        return False
    local, dom = s.split("@")
    if local == "":
        return False
    parts = dom.split(".")
    return len(parts) >= 2 and all(p != "" for p in parts)


def status(field, v):
    if v == "":
        return "missing"
    if field == "name":
        if len(v) > 20:
            return "too long"
    elif field == "age":
        if not all_digits(v):
            return "not a number"
        if len(v) > 3 or int(v) > 120:
            return "out of range"
    elif field == "email":
        if not email_ok(v):
            return "invalid"
    elif not (len(v) == 5 and all_digits(v)):
        return "invalid"
    return "ok"


def main():
    values = {}
    for i, line in enumerate(sys.stdin.read().splitlines()):
        if line.strip() == "":
            continue
        eq = line.find("=")
        if eq < 0:
            print(f"line {i + 1}: malformed")
            continue
        key = line[:eq].strip()
        if key not in FIELDS:
            print(f"line {i + 1}: unknown field {key}")
            continue
        values[key] = line[eq + 1:].strip()
    bad = 0
    for f in FIELDS:
        st = status(f, values.get(f, ""))
        if st != "ok":
            bad += 1
        print(f"{f}: {st}")
    if bad == 0:
        print("RESULT valid")
    else:
        print(f"RESULT invalid ({bad})")


main()

import sys


def is_symbol(c):
    return not c.isalnum() and c != " "


def has_repeat(cs):
    for i in range(2, len(cs)):
        if cs[i] == cs[i - 1] and cs[i] == cs[i - 2]:
            return True
    return False


def broken_rules(pw):
    out = []
    if len(pw) < 8:
        out.append("short")
    if not any("A" <= c <= "Z" for c in pw):
        out.append("no-upper")
    if not any("a" <= c <= "z" for c in pw):
        out.append("no-lower")
    if not any("0" <= c <= "9" for c in pw):
        out.append("no-digit")
    if not any(is_symbol(c) for c in pw):
        out.append("no-symbol")
    if " " in pw:
        out.append("space")
    if has_repeat(pw):
        out.append("repeat")
    return out


def main():
    for line in sys.stdin.read().splitlines():
        if line == "":
            continue
        rules = broken_rules(line)
        if not rules:
            print(f"{line}: OK")
        else:
            print(f"{line}: FAIL {','.join(rules)}")


main()

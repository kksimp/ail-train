import sys


def parse_amount(s):
    body = s[1:] if s.startswith("-") else s
    if body == "" or not all("0" <= c <= "9" for c in body):
        return None
    n = int(s)
    if n <= 0:
        return None
    return n


def report(accts):
    if not accts:
        return ["no customers"]
    return [f"{name} {accts[name][1]}/{accts[name][0]}" for name in sorted(accts)]


def handle(accts, n, line):
    w = line.split()
    cmd = w[0]
    if cmd == "report" and len(w) == 1:
        return report(accts)
    if len(w) != 3 or cmd not in ("limit", "order", "pay"):
        return [f"ERROR line {n}: bad command"]
    amt = parse_amount(w[2])
    if amt is None:
        return [f"ERROR line {n}: bad amount"]
    name = w[1]
    if cmd == "limit":
        if name in accts:
            accts[name][0] = amt
        else:
            accts[name] = [amt, 0]
        return [f"LIMIT {name} {amt}"]
    if name not in accts:
        return [f"REJECT {name}: unknown customer"]
    limit, used = accts[name]
    if cmd == "order":
        total = used + amt
        if total > limit:
            return [f"REJECT {name} {amt}: over limit by {total - limit}"]
        accts[name][1] = total
        return [f"ACCEPT {name} {amt} balance {total}/{limit}"]
    if amt > used:
        return [f"REJECT {name} {amt}: overpayment"]
    accts[name][1] = used - amt
    return [f"PAID {name} {amt} balance {used - amt}/{limit}"]


def main():
    accts = {}
    for i, line in enumerate(sys.stdin.read().splitlines()):
        if line.strip() == "":
            continue
        for out in handle(accts, i + 1, line):
            print(out)


main()

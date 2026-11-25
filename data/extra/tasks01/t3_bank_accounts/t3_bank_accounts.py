import sys


def amount(s):
    s = s.strip()
    if s.lstrip("-").isdigit() and s != "-" and s.isascii():
        n = int(s)
        if n >= 1:
            return n
    return None


def run(acc, w):
    c = w[0]
    counts = {"open": 2, "deposit": 3, "withdraw": 3, "transfer": 4, "balance": 2, "report": 1}
    if c not in counts or len(w) != counts[c]:
        return "error: bad command"
    if c == "report":
        out = [f"{n} {acc[n]}" for n in sorted(acc)]
        out.append(f"total {sum(acc.values())}")
        return "\n".join(out)
    if c == "open":
        if w[1] in acc:
            return f"error: exists {w[1]}"
        acc[w[1]] = 0
        return f"opened {w[1]}"
    if c == "balance":
        if w[1] not in acc:
            return f"error: no such account {w[1]}"
        return f"{w[1]}: {acc[w[1]]}"
    amt = amount(w[-1])
    if amt is None:
        return "error: bad amount"
    for n in w[1:-1]:
        if n not in acc:
            return f"error: no such account {n}"
    if c == "deposit":
        acc[w[1]] += amt
        return f"{w[1]}: {acc[w[1]]}"
    if c == "withdraw":
        if acc[w[1]] < amt:
            return "error: insufficient funds"
        acc[w[1]] -= amt
        return f"{w[1]}: {acc[w[1]]}"
    if w[1] == w[2]:
        return "error: same account"
    if acc[w[1]] < amt:
        return "error: insufficient funds"
    acc[w[1]] -= amt
    acc[w[2]] += amt
    return f"{w[1]}->{w[2]} {amt}"


def main():
    acc = {}
    for line in sys.stdin.read().split("\n"):
        w = line.split()
        if w:
            print(run(acc, w))


main()

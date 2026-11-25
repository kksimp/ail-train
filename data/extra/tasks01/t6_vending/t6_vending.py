import sys
DENOMS = [100, 25, 10, 5]
def pay(amount, bank):
    left = amount
    out = []
    for d in DENOMS:
        k = min(left // d, bank[d])
        out += [d] * k
        left -= k * d
    return out if left == 0 else None
def text(cs):
    return "+".join(map(str, cs)) if cs else "none"
def main():
    lines = sys.stdin.read().split("\n")
    if lines and lines[-1] == "":
        lines.pop()
    bank = {d: 0 for d in DENOMS}
    price, qty = {}, {}
    credit = 0
    for line in lines:
        w = line.strip().split()
        cmd = w[0] if w else ""
        def isnum(s):
            try:
                int(s)
                return True
            except ValueError:
                return False
        if cmd == "stock" and len(w) == 4 and isnum(w[2]) and isnum(w[3]) and int(w[2]) > 0 and int(w[3]) >= 1:
            price[w[1]] = int(w[2])
            qty[w[1]] = qty.get(w[1], 0) + int(w[3])
        elif cmd == "coin" and len(w) == 2 and isnum(w[1]):
            c = int(w[1])
            if c in bank:
                bank[c] += 1
                credit += c
                print("credit=%d" % credit)
            else:
                print("rejected %d" % c)
        elif cmd == "select" and len(w) == 2:
            n = w[1]
            if n not in price:
                print("unknown " + n)
            elif qty[n] == 0:
                print("sold out " + n)
            elif credit < price[n]:
                print("need %d more" % (price[n] - credit))
            else:
                cs = pay(credit - price[n], bank)
                if cs is None:
                    print("no change")
                else:
                    for c in cs:
                        bank[c] -= 1
                    qty[n] -= 1
                    credit = 0
                    print("vend %s change=%s" % (n, text(cs)))
        elif cmd == "refund" and len(w) == 1:
            cs = pay(credit, bank)
            if cs is None:
                print("no change")
            else:
                for c in cs:
                    bank[c] -= 1
                credit = 0
                print("refund " + text(cs))
        else:
            print("bad command")
    print("credit=%d" % credit)
    for n in sorted(price):
        print("stock %s %d" % (n, qty[n]))
main()

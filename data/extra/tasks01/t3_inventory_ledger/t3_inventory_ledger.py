import sys


def num(s, lo):
    if s.isascii() and s.lstrip("-").isdigit() and s != "-":
        n = int(s)
        if n >= lo:
            return n
    return None


def main():
    lines = sys.stdin.read().split("\n")
    if lines[-1] == "":
        lines.pop()
    onhand, tin, tout = {}, {}, {}
    for k, line in enumerate(lines, 1):
        w = line.split()
        if not w:
            continue
        c = w[0]
        want = {"receive": 3, "ship": 3, "adjust": 3, "stock": 2, "low": 2, "report": 1}
        if c not in want or len(w) != want[c]:
            print(f"line {k}: bad command")
            continue
        if c == "report":
            for s in sorted(onhand):
                print(f"{s} {onhand[s]} {tin[s]} {tout[s]}")
            print(f"skus {len(onhand)}")
            continue
        if c == "low":
            n = num(w[1], 0)
            if n is None:
                print(f"line {k}: bad quantity")
                continue
            rows = [s for s in sorted(onhand) if onhand[s] < n]
            if not rows:
                print("none")
            for s in rows:
                print(f"{s} {onhand[s]}")
            continue
        sku = w[1]
        if c == "stock":
            if sku not in onhand:
                print(f"line {k}: unknown SKU")
            else:
                print(f"{sku}: {onhand[sku]}")
            continue
        q = num(w[2], 0 if c == "adjust" else 1)
        if q is None:
            print(f"line {k}: bad quantity")
            continue
        if c == "ship":
            if sku not in onhand:
                print(f"line {k}: unknown SKU")
                continue
            if onhand[sku] < q:
                print(f"line {k}: short {sku}: have {onhand[sku]}, need {q}")
                continue
        if sku not in onhand:
            onhand[sku], tin[sku], tout[sku] = 0, 0, 0
        if c == "receive":
            onhand[sku] += q
            tin[sku] += q
        elif c == "ship":
            onhand[sku] -= q
            tout[sku] += q
        else:
            onhand[sku] = q
        print(f"{sku}: {onhand[sku]}")


main()

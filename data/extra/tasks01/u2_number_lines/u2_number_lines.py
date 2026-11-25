import sys

def main():
    lines = sys.stdin.read().splitlines()
    out = []
    n = 0
    pending = False
    started = False
    for ln in lines:
        if ln.strip(" \t") == "":
            if started:
                pending = True
        else:
            if pending:
                out.append("")
                pending = False
            n += 1
            out.append(f"{n:>4}  {ln}")
            started = True
    for o in out:
        print(o)
    print(f"-- {n} numbered lines")

main()

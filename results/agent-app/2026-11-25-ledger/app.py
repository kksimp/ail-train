import sys, re

KINDS = ["asset", "liability", "income", "expense"]
NAME_RE = re.compile(r"[A-Za-z][A-Za-z0-9_-]{0,11}")
AMT_RE = re.compile(r"(-?)([0-9]{1,11})(?:\.([0-9]{2}))?")
ARGC = {"OPEN": 2, "POST": 2, "MOVE": 3, "CLOSE": 1, "REPORT": 0}


def parse_amount(tok):
    m = AMT_RE.fullmatch(tok)
    if not m:
        return None
    v = int(m.group(2)) * 100 + (int(m.group(3)) if m.group(3) else 0)
    if v > 10 ** 12:
        return None
    return -v if m.group(1) else v


def fmt(c):
    s = "-" if c < 0 else ""
    a = abs(c)
    return "%s%d.%02d" % (s, a // 100, a % 100)


def row(a, b, c, d):
    return a.ljust(12) + " " + b.ljust(9) + " " + c.rjust(5) + " " + d.rjust(16)


def main():
    data = sys.stdin.buffer.read().decode("ascii", errors="replace")
    lines = data.split("\n")
    if lines and lines[-1] == "":
        lines.pop()
    out = []
    accts = {}  # name -> [kind, balance, posts]
    ok = 0
    errs = 0
    for i, line in enumerate(lines, 1):
        toks = [t for t in re.split(r"[ \t]+", line) if t != ""]
        if not toks or toks[0].startswith("#"):
            continue
        cmd, args = toks[0], toks[1:]

        def err(msg):
            out.append("line %d: error: %s" % (i, msg))

        e = None
        if cmd not in ARGC:
            e = "unknown command"
        elif len(args) != ARGC[cmd]:
            e = "wrong argument count"
        elif cmd == "OPEN":
            name, kind = args
            if not NAME_RE.fullmatch(name):
                e = "bad name"
            elif kind not in KINDS:
                e = "bad kind"
            elif name in accts:
                e = "duplicate account"
            else:
                accts[name] = [kind, 0, 0]
        elif cmd == "POST":
            name, at = args
            if name not in accts:
                e = "unknown account"
            else:
                v = parse_amount(at)
                if v is None:
                    e = "bad amount"
                else:
                    accts[name][1] += v
                    accts[name][2] += 1
        elif cmd == "MOVE":
            f, t, at = args
            if f not in accts or t not in accts:
                e = "unknown account"
            elif f == t:
                e = "same account"
            else:
                v = parse_amount(at)
                if v is None:
                    e = "bad amount"
                elif v <= 0:
                    e = "amount must be positive"
                else:
                    accts[f][1] -= v
                    accts[f][2] += 1
                    accts[t][1] += v
                    accts[t][2] += 1
        elif cmd == "CLOSE":
            name = args[0]
            if name not in accts:
                e = "unknown account"
            elif accts[name][1] != 0:
                e = "nonzero balance"
            else:
                del accts[name]
        elif cmd == "REPORT":
            out.append(row("ACCOUNT", "KIND", "POSTS", "BALANCE"))
            items = sorted(accts.items(), key=lambda kv: (KINDS.index(kv[1][0]), -kv[1][1], kv[0]))
            tp = 0
            tb = 0
            for n, (k, b, p) in items:
                out.append(row(n, k, str(p), fmt(b)))
                tp += p
                tb += b
            out.append(row("TOTAL", "", str(tp), fmt(tb)))
        if e is None:
            ok += 1
        else:
            err(e)
            errs += 1
    out.append("ok=%d errors=%d" % (ok, errs))
    sys.stdout.write("\n".join(out) + "\n")


main()

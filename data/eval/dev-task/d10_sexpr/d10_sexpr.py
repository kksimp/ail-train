import re
import sys

OPS = {"+", "-", "*", "/", "min", "max"}


class Err(Exception):
    pass


def tokenize(s):
    toks = re.findall(r"[()]|[^()\s]+", s)
    return toks


def parse(toks, i):
    if i >= len(toks):
        raise Err("syntax error")
    t = toks[i]
    i += 1
    if t == "(":
        if i >= len(toks) or toks[i] not in OPS:
            raise Err("syntax error")
        op = toks[i]
        i += 1
        args = []
        while i < len(toks) and toks[i] != ")":
            a, i = parse(toks, i)
            args.append(a)
        if i >= len(toks):
            raise Err("syntax error")
        return (op, args), i + 1
    if re.fullmatch(r"-?[0-9]+", t):
        return int(t), i
    raise Err("syntax error")


def ev(node):
    if isinstance(node, int):
        return node
    op, args = node
    vals = [ev(a) for a in args]
    if not vals or (op == "/" and len(vals) != 2):
        raise Err("bad arity")
    if op == "+":
        return sum(vals)
    if op == "*":
        r = 1
        for x in vals:
            r *= x
        return r
    if op == "min":
        return min(vals)
    if op == "max":
        return max(vals)
    if op == "/":
        if vals[1] == 0:
            raise Err("division by zero")
        q = abs(vals[0]) // abs(vals[1])
        return q if (vals[0] < 0) == (vals[1] < 0) else -q
    if len(vals) == 1:
        return -vals[0]
    return vals[0] - sum(vals[1:])


for n, line in enumerate(sys.stdin.read().splitlines(), 1):
    if not line.strip():
        continue
    try:
        toks = tokenize(line)
        root, pos = parse(toks, 0)
        if pos != len(toks):
            raise Err("syntax error")
        print("%d: %d" % (n, ev(root)))
    except Err as e:
        print("%d: error: %s" % (n, e))

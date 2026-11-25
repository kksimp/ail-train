import sys

class P:
    def __init__(self, toks, vals):
        self.toks = toks
        self.pos = 0
        self.vals = vals
        self.bad = False

    def peek(self):
        return self.toks[self.pos] if self.pos < len(self.toks) else "$"

    def parse_or(self):
        v = self.parse_xor()
        while self.peek() == "|":
            self.pos += 1
            r = self.parse_xor()
            v = v | r
        return v

    def parse_xor(self):
        v = self.parse_and()
        while self.peek() == "^":
            self.pos += 1
            r = self.parse_and()
            v = v ^ r
        return v

    def parse_and(self):
        v = self.parse_not()
        while self.peek() == "&":
            self.pos += 1
            r = self.parse_not()
            v = v & r
        return v

    def parse_not(self):
        t = self.peek()
        if t == "!":
            self.pos += 1
            return 1 - self.parse_not()
        if t == "(":
            self.pos += 1
            v = self.parse_or()
            if self.peek() == ")":
                self.pos += 1
            else:
                self.bad = True
            return v
        if t in ("0", "1"):
            self.pos += 1
            return int(t)
        if "a" <= t <= "z":
            self.pos += 1
            return self.vals[ord(t) - 97]
        self.bad = True
        return 0

def run(toks, vals):
    p = P(toks, vals)
    v = p.parse_or()
    if p.pos != len(toks):
        p.bad = True
    return v, p.bad

for raw in sys.stdin.read().splitlines():
    line = raw.strip()
    if line == "":
        continue
    print("expr: " + line)
    toks = [c for c in line if c != " "]
    if any(not (("a" <= c <= "z") or c in "01!&|^()") for c in toks):
        print("syntax error")
        continue
    v, bad = run(toks, [0] * 26)
    if bad:
        print("syntax error")
        continue
    used = sorted(set(c for c in toks if "a" <= c <= "z"))
    n = len(used)
    if n > 4:
        print("too many variables")
        continue
    ones = 0
    if n == 0:
        print("f = %d" % v)
        ones = v
    else:
        print(" ".join(used) + " | f")
    for m in range(1 << n if n > 0 else 0):
        vals = [0] * 26
        bits = []
        for j in range(n):
            b = (m >> (n - 1 - j)) & 1
            vals[ord(used[j]) - 97] = b
            bits.append(str(b))
        r, _ = run(toks, vals)
        ones += r
        print(" ".join(bits) + " | " + str(r))
    total = 1 if n == 0 else 1 << n
    print("tautology" if ones == total else "contradiction" if ones == 0 else "contingent")

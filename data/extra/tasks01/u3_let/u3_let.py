import sys

KEYWORDS = ("let", "in")

class Interp:
    def __init__(self, toks):
        self.toks = toks
        self.pos = 0
        self.names = []
        self.vals = []
        self.err = ""

    def peek(self):
        return self.toks[self.pos] if self.pos < len(self.toks) else ""

    def fail(self, msg):
        if self.err == "":
            self.err = msg
        self.pos = len(self.toks)

    def is_name(self, t):
        return t != "" and t.isascii() and t.isalpha() and t.islower() and t not in KEYWORDS

    def parse_expr(self):
        if self.peek() == "let":
            self.pos += 1
            name = self.peek()
            if not self.is_name(name):
                self.fail("syntax")
                return 0
            self.pos += 1
            if self.peek() != "=":
                self.fail("syntax")
                return 0
            self.pos += 1
            v = self.parse_expr()
            if self.err != "":
                return 0
            if self.peek() != "in":
                self.fail("syntax")
                return 0
            self.pos += 1
            self.names.append(name)
            self.vals.append(v)
            r = self.parse_expr()
            self.names.pop()
            self.vals.pop()
            return r
        return self.parse_sum()

    def check(self, v):
        if abs(v) > 1000000000000:
            self.fail("overflow")
            return 0
        return v

    def parse_sum(self):
        v = self.parse_term()
        while self.peek() in ("+", "-"):
            op = self.peek()
            self.pos += 1
            r = self.parse_term()
            if self.err != "":
                return 0
            v = self.check(v + r if op == "+" else v - r)
        return v

    def parse_term(self):
        v = self.parse_unary()
        while self.peek() in ("*", "/", "%"):
            op = self.peek()
            self.pos += 1
            r = self.parse_unary()
            if self.err != "":
                return 0
            if op == "*":
                v = self.check(v * r)
            elif r == 0:
                self.fail("division by zero")
                return 0
            else:
                q = abs(v) // abs(r)
                if (v < 0) != (r < 0):
                    q = -q
                v = q if op == "/" else v - q * r
        return v

    def parse_unary(self):
        if self.peek() == "-":
            self.pos += 1
            return -self.parse_unary()
        return self.parse_atom()

    def parse_atom(self):
        t = self.peek()
        if t != "" and t[0].isdigit():
            self.pos += 1
            return int(t)
        if t == "(":
            self.pos += 1
            v = self.parse_expr()
            if self.peek() == ")":
                self.pos += 1
            else:
                self.fail("syntax")
            return v
        if self.is_name(t):
            self.pos += 1
            for i in range(len(self.names) - 1, -1, -1):
                if self.names[i] == t:
                    return self.vals[i]
            self.fail("unbound " + t)
            return 0
        self.fail("syntax")
        return 0

def tokenize(line):
    toks = []
    i = 0
    while i < len(line):
        c = line[i]
        if c == " ":
            i += 1
        elif "0" <= c <= "9":
            j = i
            while j < len(line) and "0" <= line[j] <= "9":
                j += 1
            if j - i > 6:
                return None
            toks.append(line[i:j])
            i = j
        elif "a" <= c <= "z":
            j = i
            while j < len(line) and "a" <= line[j] <= "z":
                j += 1
            toks.append(line[i:j])
            i = j
        elif c in "+-*/%()=":
            toks.append(c)
            i += 1
        else:
            return None
    return toks

for raw in sys.stdin.read().splitlines():
    line = raw.strip()
    if line == "":
        continue
    toks = tokenize(line)
    if toks is None:
        print("error: syntax")
        continue
    p = Interp(toks)
    v = p.parse_expr()
    if p.err == "" and p.pos != len(toks):
        p.err = "syntax"
    print(v if p.err == "" else "error: " + p.err)

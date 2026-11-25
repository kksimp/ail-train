import sys

class Syn(Exception): pass
class Div0(Exception): pass

class P:
    def __init__(self, s):
        self.s = s; self.i = 0
        self.div0 = False
    def peek(self):
        while self.i < len(self.s) and self.s[self.i] == ' ':
            self.i += 1
        return self.s[self.i] if self.i < len(self.s) else None
    def expr(self):
        v = self.term()
        while self.peek() in ('+', '-'):
            c = self.s[self.i]; self.i += 1
            r = self.term()
            v = v + r if c == '+' else v - r
        return v
    def term(self):
        v = self.atom()
        while self.peek() in ('*', '/'):
            c = self.s[self.i]; self.i += 1
            r = self.atom()
            if c == '*':
                v = v * r
            elif r == 0:
                self.div0 = True
                v = 0
            else:
                q = abs(v) // abs(r)
                v = q if (v < 0) == (r < 0) else -q
        return v
    def atom(self):
        c = self.peek()
        if c == '-':
            self.i += 1
            return -self.atom()
        if c == '(':
            self.i += 1
            v = self.expr()
            if self.peek() != ')':
                raise Syn()
            self.i += 1
            return v
        if c is not None and c.isdigit():
            j = self.i
            while j < len(self.s) and self.s[j].isdigit():
                j += 1
            v = int(self.s[self.i:j]); self.i = j
            return v
        raise Syn()

for line in sys.stdin.read().split("\n"):
    if line.strip(" ") == "":
        continue
    p = P(line)
    try:
        v = p.expr()
        if p.peek() is not None:
            raise Syn()
        print("div0" if p.div0 else v)
    except Syn:
        print("error")

class Stall:
    def __init__(self, items, op, arg, div, yes, no):
        self.items, self.op, self.arg, self.div, self.yes, self.no, self.seen = list(items), op, arg, div, yes, no, 0
    def apply(self, v):
        if self.op == "plus": return v + self.arg
        if self.op == "times": return v * self.arg
        return v * v

def make():
    return [Stall([61, 22, 85], "times", 3, 7, 2, 1), Stall([40, 91], "plus", 6, 11, 3, 0), Stall([17, 50, 73, 9], "square", 0, 13, 1, 3), Stall([33], "plus", 4, 17, 0, 2)]

def play(stalls, rounds, calm):
    modulus = 1
    for s in stalls:
        modulus *= s.div
    for _ in range(rounds):
        for st in stalls:
            held = st.items; st.items = []
            st.seen += len(held)
            for v in held:
                w = st.apply(v)
                w = w // 3 % modulus if calm else w % modulus
                to = st.yes if w % st.div == 0 else st.no
                stalls[to].items.append(w)
    counts = sorted([s.seen for s in stalls], reverse=True)
    print(f"  inspections: {counts}")
    return counts[0] * counts[1]

st = make()
print(f"{len(st)} stalls, {sum(len(s.items) for s in st)} items")
print(f"part 1, 20 calm rounds: {play(make(), 20, True)}")
print(f"part 2, 600 tense rounds: {play(make(), 600, False)}")

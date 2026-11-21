C = ["red", "teal", "amber", "plum", "navy", "olive"]
def ini(n):
    w = n.split()
    if not w: return "?"
    a = w[0][0]
    if len(w) == 1:
        b = w[0][1] if len(w[0]) > 1 else " "
        return f"{a.upper()}{b}".strip()
    return f"{a.upper()}{w[-1][0].upper()}"
def col(n): return C[sum(ord(c) for c in n) % 6]
for n in ["ada lovelace", "Grace Brewster Hopper", "linus", "  ", "Zoë Kravitz", "x"]:
    s = "(blank)" if n.strip() == "" else n
    print(f"{s:<22} {ini(n):<3} {col(n)}")

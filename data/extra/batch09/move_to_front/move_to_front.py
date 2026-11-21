def encode(s):
    table = list("abcdefghijklmnopqrstuvwxyz")
    out = []
    for c in s:
        at = table.index(c)
        out.append(at)
        table.pop(at)
        table.insert(0, c)
    return out

def decode(codes):
    table = list("abcdefghijklmnopqrstuvwxyz")
    out = []
    for at in codes:
        c = table[at]
        out.append(c)
        table.pop(at)
        table.insert(0, c)
    return "".join(out)

for s in ["bananaaa", "aaabbbccc", "abcabcabc", "nnbaaa", "zzzzzy"]:
    codes = encode(s)
    zeros = sum(1 for c in codes if c == 0)
    shown = " ".join(str(c) for c in codes)
    back = decode(codes)
    print(f"{s:<10} {shown:<26} zeros {zeros}, sum {sum(codes):>3}, decodes to {back}")

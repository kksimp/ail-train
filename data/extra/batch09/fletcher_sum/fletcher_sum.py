def sums(bs):
    a = 0
    b = 0
    for x in bs:
        a = (a + x) % 255
        b = (b + a) % 255
    return [a, b]

def fletcher(bs):
    s = sums(bs)
    return (s[1] << 8) | s[0]

def codes(s):
    return [ord(c) for c in s]

for s in ["abcde", "abcdef", "abcdefgh", "bacde"]:
    bs = codes(s)
    plain = sum(bs) % 256
    print(f"{s:<9} fletcher {fletcher(bs):04x}, plain sum {plain:02x}")
msg = codes("hello")
s = sums(msg)
c0 = 255 - (s[0] + s[1]) % 255
c1 = 255 - (s[0] + c0) % 255
sent = msg + [c0, c1]
check = sums(sent)
print(f"hello + check bytes {c0:02x} {c1:02x}: sums {check[0]} and {check[1]}")

ALPHABET = "123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz"

def encode(bs):
    num = list(bs)
    out = []
    lead = 0
    while lead < len(bs) and bs[lead] == 0:
        lead += 1
    start = lead
    while start < len(num):
        rem = 0
        for i in range(start, len(num)):
            acc = rem * 256 + num[i]
            num[i] = acc // 58
            rem = acc % 58
        out.append(ALPHABET[rem])
        while start < len(num) and num[start] == 0:
            start += 1
    out.extend(['1'] * lead)
    out.reverse()
    return "".join(out)

def decode(text):
    num = []
    lead = 0
    for c in text:
        if not num and c == '1':
            lead += 1
            continue
        carry = ALPHABET.find(c)
        i = len(num) - 1
        while i >= 0:
            acc = num[i] * 58 + carry
            num[i] = acc % 256
            carry = acc // 256
            i -= 1
        while carry > 0:
            num.insert(0, carry % 256)
            carry = carry // 256
    return [0] * lead + num

for s in ["Hello World!", "hello", "abc", "a"]:
    bs = [ord(c) for c in s]
    e = encode(bs)
    back = "".join(chr(b) for b in decode(e))
    print(f"{s:<13} -> {e:<18} back '{back}'")
raw = [0, 0, 1, 255, 16]
e = encode(raw)
print(f"bytes {raw} -> {e} -> {decode(e)}")

def letter(n):
    return chr((n % 26 + 26) % 26 + 65)

def encrypt(msg, primer):
    key = list(primer) + list(msg)
    return "".join(letter(ord(msg[i]) + ord(key[i]) - 130) for i in range(len(msg)))

def decrypt(code, primer):
    key = list(primer)
    out = []
    for i in range(len(code)):
        c = letter(ord(code[i]) - ord(key[i]))
        out.append(c)
        key.append(c)
    return "".join(out)

pairs = [("ATTACKATDAWN", "QUEENLY"), ("HELLOTHERE", "KEY"), ("SENDMOREMONEY", "ZEBRA")]
for msg, primer in pairs:
    code = encrypt(msg, primer)
    back = decrypt(code, primer)
    print(f"{msg:<14} key {primer:<8} -> {code:<14} -> {back}")
print("key stream for the first: QUEENLYATTAC...")

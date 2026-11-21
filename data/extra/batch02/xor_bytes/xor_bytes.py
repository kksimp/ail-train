key = b"k3y"
x = lambda d: bytes(d[i] ^ key[i % len(key)] for i in range(len(d)))
for m in ["attack at dawn", "hello", ""]:
    e = x(m.encode())
    print(f"'{m}' -> {e.hex()} -> '{x(bytes.fromhex(e.hex())).decode()}'")

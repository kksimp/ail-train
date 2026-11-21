def crc8(d):
    c = 0
    for x in d:
        c ^= x
        for _ in range(8):
            c = ((c << 1) ^ 7) & 255 if c & 128 else (c << 1) & 255
    return c
for m in ["123456789", "hello", "hellp", "", "AAAA"]:
    print(f"{crc8(m.encode()):02x} {m}")
print(f"corruption detected: {str(crc8(b'transfer 100 to bob') != crc8(b'transfer 900 to bob')).lower()}")

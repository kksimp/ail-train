import base64
def xs(d):
    x = 0
    for b in d: x ^= b
    return x
for p in ["HELLO", "ping 42", ""]:
    d = p.encode()
    print(f"'{p}': {len(d)} bytes, hex [{d.hex(' ')}], xor {xs(d):02x}, sum {sum(d) % 256:02x}")
r = bytes.fromhex("deadbeef")
print(f"{len(r)} bytes: xor {xs(r):02x}, sum {sum(r) % 256:02x}")
print("true")
print(base64.b64encode(b"AB").decode())

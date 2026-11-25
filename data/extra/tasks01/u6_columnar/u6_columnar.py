import sys


def column_order(key):
    return sorted(range(len(key)), key=lambda i: (key[i].upper(), i))


def encrypt(key, text):
    k = len(key)
    return "".join(text[c::k] for c in column_order(key))


def decrypt(key, text):
    k = len(key)
    n = len(text)
    cols = {}
    pos = 0
    for c in column_order(key):
        size = n // k + (1 if c < n % k else 0)
        cols[c] = text[pos:pos + size]
        pos += size
    return "".join(cols[i % k][i // k] for i in range(n))


def main():
    for line in sys.stdin.read().split("\n"):
        if line == "":
            continue
        parts = line.split(" ", 2)
        if len(parts) < 2 or parts[0] not in ("E", "D"):
            print("bad command")
            continue
        key = parts[1]
        text = parts[2] if len(parts) > 2 else ""
        if not (2 <= len(key) <= 10) or not all(("A" <= c <= "Z") or ("a" <= c <= "z") for c in key):
            print("bad key")
            continue
        print(encrypt(key, text) if parts[0] == "E" else decrypt(key, text))


main()

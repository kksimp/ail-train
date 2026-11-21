def order(key):
    return sorted(range(len(key)), key=lambda i: (ord(key[i]), i))

def encrypt(msg, key):
    cols = len(key)
    letters = [c for c in msg if c.isalpha()]
    while len(letters) % cols != 0:
        letters.append('X')
    rows = len(letters) // cols
    out = []
    for c in order(key):
        for r in range(rows):
            out.append(letters[r * cols + c])
    return "".join(out)

def decrypt(code, key):
    cols = len(key)
    rows = len(code) // cols
    grid = [' '] * len(code)
    at = 0
    for c in order(key):
        for r in range(rows):
            grid[r * cols + c] = code[at]
            at += 1
    return "".join(grid)

key = "ZEBRAS"
shown = " ".join(str(i + 1) for i in order(key))
print(f"key {key}: columns read in order {shown}")
msg = "WEAREDISCOVEREDFLEEATONCE"
code = encrypt(msg, key)
print(f"{msg} -> {code}")
print(f"decrypted: {decrypt(code, key)}")
second = encrypt("MEETATTHEBRIDGE", "SECRET")
print(f"MEETATTHEBRIDGE with SECRET -> {second} -> {decrypt(second, 'SECRET')}")

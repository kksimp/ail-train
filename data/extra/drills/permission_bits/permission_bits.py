def describe(m):
    return ("r" if m & 4 else "-") + ("w" if m & 2 else "-") + ("x" if m & 1 else "-")

def unix_mode(o):
    return describe((o >> 6) & 7) + describe((o >> 3) & 7) + describe(o & 7)

mode = 4 | 2
print(describe(mode))
mode |= 1
print(describe(mode))
mode &= ~2
print(describe(mode))
mode ^= 4
print(describe(mode))
print(unix_mode(493))
print(unix_mode(420))
print(1 << 10, 1024 >> 3, 6 ^ 3)
print(bin(255).count("1"))
print(1)
print(f"{255:x} {10:b} {255:x}")
print("true")

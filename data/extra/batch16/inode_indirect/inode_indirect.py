def locate(off):
    b = off // 1024
    if b < 12:
        return f"direct[{b}], 1 block read"
    b -= 12
    if b < 256:
        return f"single[{b}], 2 block reads"
    b -= 256
    if b < 65536:
        return f"double[{b // 256}][{b % 256}], 3 block reads"
    b -= 65536
    return f"triple[{b // 65536}][{b // 256 % 256}][{b % 256}], 4 block reads"

for off in [0, 11264, 12287, 12288, 274431, 274432, 5000000, 67383296, 70000000]:
    print(f"byte {off:>10,} -> {locate(off)}")
blocks = 12 + 256 + 65536 + 16777216
print(f"largest file: {blocks:,} blocks = {blocks * 1024:,} bytes")

import sys

data = sys.stdin.buffer.read()
for off in range(0, len(data), 16):
    chunk = data[off:off + 16]
    hexes = " ".join("%02x" % b for b in chunk).ljust(47)
    asc = "".join(chr(b) if 32 <= b <= 126 else "." for b in chunk)
    print("%08x  %s  |%s|" % (off, hexes, asc))
print("%08x" % len(data))

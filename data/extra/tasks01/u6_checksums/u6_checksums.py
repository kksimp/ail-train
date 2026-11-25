import sys


def adler(data):
    a, b = 1, 0
    for x in data:
        a = (a + x) % 65521
        b = (b + a) % 65521
    return b * 65536 + a


def crc8(data):
    crc = 0
    for x in data:
        crc ^= x
        for _ in range(8):
            if crc & 0x80:
                crc = ((crc << 1) ^ 0x07) & 0xFF
            else:
                crc = (crc << 1) & 0xFF
    return crc


def main():
    text = sys.stdin.read()
    lines = text.split("\n")
    if lines and lines[-1] == "":
        lines.pop()
    for line in lines:
        data = line.encode("ascii")
        print("adler32=%08x crc8=%02x" % (adler(data), crc8(data)))
    print("lines=%d" % len(lines))


main()

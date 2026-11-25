import sys


def crypt(mode, key, text):
    shifts = [ord(k.upper()) - 65 for k in key]
    sign = 1 if mode == "E" else -1
    out = []
    j = 0
    for c in text:
        if "A" <= c <= "Z" or "a" <= c <= "z":
            base = 65 if c <= "Z" else 97
            out.append(chr((ord(c) - base + sign * shifts[j % len(shifts)]) % 26 + base))
            j += 1
        else:
            out.append(c)
    return "".join(out)


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
        if key == "" or not all(("A" <= c <= "Z") or ("a" <= c <= "z") for c in key):
            print("bad key")
            continue
        print(crypt(parts[0], key, text))


main()

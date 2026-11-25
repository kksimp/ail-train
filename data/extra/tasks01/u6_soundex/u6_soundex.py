import sys

DIGITS = {}
for letters, d in (("BFPV", "1"), ("CGJKQSXZ", "2"), ("DT", "3"), ("L", "4"), ("MN", "5"), ("R", "6")):
    for ch in letters:
        DIGITS[ch] = d


def soundex(word):
    letters = [c.upper() for c in word if ("A" <= c <= "Z") or ("a" <= c <= "z")]
    if not letters:
        return "----"
    out = letters[0]
    prev = DIGITS.get(letters[0], "")
    for c in letters[1:]:
        if c in "HW":
            continue
        d = DIGITS.get(c, "")
        if d != "" and d != prev:
            out += d
        prev = d
    return (out + "000")[:4]


def main():
    for line in sys.stdin.read().split("\n"):
        if line == "":
            continue
        words = [w for w in line.split(" ") if w != ""]
        if words:
            print(" ".join(soundex(w) for w in words))
        else:
            print("")


main()

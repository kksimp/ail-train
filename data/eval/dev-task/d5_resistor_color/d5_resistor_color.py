import sys

DIGITS = ["black", "brown", "red", "orange", "yellow", "green", "blue", "violet", "grey", "white"]
TOL = {"brown": "1", "red": "2", "green": "0.5", "blue": "0.25", "violet": "0.1",
       "grey": "0.05", "gold": "5", "silver": "10"}

for k, line in enumerate(sys.stdin.read().splitlines(), 1):
    w = line.split()
    if not w:
        continue
    if len(w) != 4 or w[0] not in DIGITS or w[1] not in DIGITS or w[3] not in TOL:
        print(f"{k}: invalid")
        continue
    if w[2] in DIGITS:
        f = 100 * 10 ** DIGITS.index(w[2])
    elif w[2] == "gold":
        f = 10
    elif w[2] == "silver":
        f = 1
    else:
        print(f"{k}: invalid")
        continue
    v = (DIGITS.index(w[0]) * 10 + DIGITS.index(w[1])) * f
    print(f"{k}: {v // 100}.{v % 100:02d} ohm +/-{TOL[w[3]]}%")

def letter(n):
    k = n + 1 if n > 7 else n
    return chr(65 + k)

def grid_ref(e, n, digits):
    e100 = e // 100000
    n100 = n // 100000
    l1 = (19 - n100) - (19 - n100) % 5 + (e100 + 10) // 5
    l2 = (19 - n100) * 5 % 25 + e100 % 5
    div = 10 ** (5 - digits)
    ee = str(e % 100000 // div).rjust(digits, '0')
    nn = str(n % 100000 // div).rjust(digits, '0')
    return f"{letter(l1)}{letter(l2)} {ee} {nn}"

places = [("Big Ben", 530047, 179951), ("Edinburgh Castle", 325130, 673470), ("Snowdon", 260950, 354370), ("Ben Nevis", 216600, 771200), ("Land's End", 134200, 25300), ("Lerwick", 447500, 1141300), ("York Minster", 460300, 452200)]
for name, e, n in places:
    print(f"{name:<17} {grid_ref(e, n, 3):<13} {grid_ref(e, n, 5)}")

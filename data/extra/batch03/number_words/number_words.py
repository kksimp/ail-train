O = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
T = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
def bh(n): return O[n] if n < 20 else T[n // 10] if n % 10 == 0 else f"{T[n // 10]}-{O[n % 10]}"
def bt(n):
    if n < 100: return bh(n)
    h = f"{bh(n // 100)} hundred"
    return h if n % 100 == 0 else f"{h} and {bh(n % 100)}"
def w(n):
    if n < 1000: return bt(n)
    h = f"{bt(n // 1000)} thousand"; r = n % 1000
    if r == 0: return h
    return h + (" and " if r < 100 else " ") + bt(r)
for n in [0, 7, 13, 40, 42, 100, 115, 999, 1000, 1005, 2024, 90210, 500000, 999999]: print(f"{n:>6}: {w(n)}")

O = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
T = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
def ut(n):
    p = []
    if n >= 100: p.append(f"{O[n // 100]} hundred")
    r = n % 100
    if r:
        if n >= 100: p.append("and")
        p.append(O[r] if r < 20 else T[r // 10] if r % 10 == 0 else f"{T[r // 10]}-{O[r % 10]}")
    return " ".join(p)
def wd(n):
    if n == 0: return "zero"
    if n >= 1000:
        h = ut(n // 1000); t = n % 1000
        if t == 0: return f"{h} thousand"
        return f"{h} thousand and {ut(t)}" if t < 100 else f"{h} thousand {ut(t)}"
    return ut(n)
for n in [0, 7, 13, 40, 99, 100, 115, 342, 1000, 1005, 2019, 12345, 700000, 999999]: print(f"{n}: {wd(n)}")

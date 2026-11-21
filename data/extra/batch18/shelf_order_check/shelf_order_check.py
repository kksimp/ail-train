shelf = [(510, "ADA", 1999), (510, "BRO", 2004), (512, "ALT", 2011), (510, "CHE", 1987), (512, "ALT", 2008), (516, "KIM", 2020), (519, "DOE", 2015)]
def label(c): return f"{c[0]} {c[1]} {c[2]}"
w = 0
for i in range(1, len(shelf)):
    if shelf[i] < shelf[i - 1]:
        w += 1; print(f"misplaced: {label(shelf[i])} after {label(shelf[i - 1])}")
print(f"{w} books out of order")
f = sorted(shelf)
print(f"first {label(f[0])}, last {label(f[-1])}")
r = (512, "ALT", 2010)
print(f"returned book {label(r)} goes at position {sum(1 for c in f if c < r) + 1}")

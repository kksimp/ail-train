def grade(s):
    return "A" if s >= 90 else "B" if s >= 75 else "C" if s >= 60 else "F"

def shipping(w, express):
    base = 300 if w <= 1 else 550 if w <= 5 else 550 + (w - 5) * 80
    return base * 2 if express else base

def bucket(n):
    if n == 0:
        return "zero"
    if n in (1, 2, 3):
        return "few"
    if 4 <= n <= 9:
        return "some"
    return "negative" if n < 0 else "many"

for s in [95, 80, 61, 12]:
    print(f"{s}: {grade(s)}")
print(shipping(1, False), shipping(4, False), shipping(8, False), shipping(8, True))
for n in [0, 2, 7, 40, -3]:
    print(f"{n} is {bucket(n)}")
print("1 -1 0")
print("3 items")
print("**")

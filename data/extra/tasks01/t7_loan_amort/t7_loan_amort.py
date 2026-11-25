import sys

def money(c):
    return f"{c // 100}.{c % 100:02d}"

def parse(text):
    for line in text.split("\n"):
        line = line.rstrip("\r")
        if line.strip() == "":
            continue
        f = [x.strip() for x in line.split(",")]
        if len(f) != 3:
            return None
        if not all(x.isascii() and x.isdigit() for x in f):
            return None
        p, r, pay = map(int, f)
        if p <= 0 or pay <= 0:
            return None
        return p, r, pay
    return None

rec = parse(sys.stdin.read())
if rec is None:
    print("invalid input")
    sys.exit(0)
bal, bp, payment = rec
if payment <= (bal * bp + 60000) // 120000:
    print("payment too small")
    sys.exit(0)
paid = 0
tot_int = 0
month = 0
while bal > 0 and month < 36:
    month += 1
    interest = (bal * bp + 60000) // 120000
    due = bal + interest
    pay = min(payment, due)
    bal = due - pay
    paid += pay
    tot_int += interest
    print(f"{month}: pay={money(pay)} interest={money(interest)} principal={money(pay - interest)} balance={money(bal)}")
if bal > 0:
    print("not repaid after 36 months")
else:
    print(f"months: {month}")
    print(f"total paid: {money(paid)}")
    print(f"total interest: {money(tot_int)}")

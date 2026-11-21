def power(b, k):
    x = 1.0
    for _ in range(k):
        x *= b
    return x

def member_value(turn, members, pay, rate):
    v = 0.0
    for t in range(members):
        v -= pay / power(1.0 + rate, t)
    return v + pay * float(members) / power(1.0 + rate, turn)

gainers = 0
for turn in range(6):
    v = member_value(turn, 6, 100.0, 0.01)
    if v > 0.0:
        gainers += 1
    role = "gains" if v > 0.0 else "gives up"
    print(f"member {turn + 1} takes the pot in month {turn + 1}: {role} {abs(v):.2f} in today's money")
print(f"{gainers} of 6 members come out ahead")

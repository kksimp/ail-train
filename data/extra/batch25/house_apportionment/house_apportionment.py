import math

states = [["Arden", 3120000, 1], ["Brook", 1840000, 1], ["Corvel", 960000, 1], ["Dunne", 655000, 1], ["Elmar", 402000, 1], ["Fallow", 118000, 1]]

def priority(s):
    n = float(s[2])
    return s[1] / math.sqrt(n * (n + 1.0))

house = 20
total = sum(s[1] for s in states)
order = []
for seat in range(len(states) + 1, house + 1):
    best = 0
    for i in range(1, len(states)):
        if priority(states[i]) > priority(states[best]):
            best = i
    order.append(f"{seat}:{states[best][0]}")
    states[best][2] += 1
print(f"seats 7 to {house}: {' '.join(order)}")
for s in states:
    quota = s[1] * float(house) / float(total)
    print(f"{s[0]:<7} {s[1]:>9,}  quota {quota:>5.2f}  seats {s[2]}")

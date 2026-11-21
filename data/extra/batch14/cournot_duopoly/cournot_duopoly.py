def reply(o):
    return (90.0 - o) / 2.0
def profit(q, o):
    return q * (100.0 - q - o - 10.0)
q1, q2 = 0.0, 20.0 / 3.0
for rnd in range(1, 9):
    q1 = reply(q2)
    q2 = reply(q1)
    print(f"round {rnd}: firm 1 makes {q1:.3f}, firm 2 makes {q2:.3f}")
print(f"Cournot: 30 each, price {100.0 - 60.0}, profit {profit(30.0, 30.0)} each")
print(f"one monopolist: makes 45, price {100.0 - 45.0}, profit {profit(45.0, 0.0)}")
print("price at cost: total 90, price 10.0, profit 0.0")
print(f"if both make 22.5 (half the monopoly) each earns {profit(22.5, 22.5)}, but one would deviate to {reply(22.5)}")

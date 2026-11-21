import math
def erlang_b(a, c):
    b = 1.0
    for k in range(1, c + 1):
        b = a * b / (float(k) + a * b)
    return b
calls_per_min = 2.0
handle_min = 4.0
a = calls_per_min * handle_min
mu = 1.0 / handle_min
print(f"{calls_per_min} calls a minute, {handle_min} minutes each: {a} erlangs")
found = 0
for c in range(9, 15):
    b = erlang_b(a, c)
    cw = b / (1.0 - a / float(c) * (1.0 - b))
    rate = float(c) * mu - calls_per_min
    wait_s = cw / rate * 60.0
    level = 1.0 - cw * math.exp(-rate * 20.0 / 60.0)
    print(f"{c:>2} agents: {cw * 100.0:>5.1f}% wait, mean wait {wait_s:>5.1f} s, {level * 100.0:>5.1f}% answered within 20 s")
    if found == 0 and level >= 0.8:
        found = c
print(f"smallest team meeting 80/20: {found} agents")

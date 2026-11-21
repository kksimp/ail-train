cap = 5; slots = [0] * cap; head = 0; count = 0
for v in [21, 22, 22, 24, 27, 31, 30, 26, 23]:
    slots[(head + count) % cap] = v
    if count == cap: head = (head + 1) % cap
    else: count += 1
    it = [slots[(head + i) % cap] for i in range(count)]
    a = sum(it) * 10 // len(it)
    print(f"{v:>3} -> {it} avg {a // 10}.{a % 10}")
print(f"raw slots {slots}, head {head}")

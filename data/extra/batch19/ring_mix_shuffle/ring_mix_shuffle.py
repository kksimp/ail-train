def mix(values, rounds):
    n = len(values); m = n - 1
    order = list(range(n))
    for _ in range(rounds):
        for i in range(n):
            pos = order.index(i)
            order.pop(pos)
            dest = ((pos + values[i]) % m + m) % m
            order.insert(dest, i)
    return [values[i] for i in order]

def grove(mixed):
    z = mixed.index(0); n = len(mixed)
    return mixed[(z + 10) % n] + mixed[(z + 20) % n] + mixed[(z + 30) % n]

code = [4, -7, 0, 12, 3, -1, 9, -15, 6, 2, -4, 8]
once = mix(code, 1)
print(f"mixed once: {once}")
print(f"part 1: key sum {grove(once)}")
four = mix([v * 1009 for v in code], 4)
print(f"part 2: key sum {grove(four)}")

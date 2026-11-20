def nxt(n):
    return sum(int(d) ** 2 for d in str(n))
def path(n):
    seen, steps, v = set(), [n], n
    while v != 1 and v not in seen:
        seen.add(v)
        v = nxt(v)
        steps.append(v)
    return v == 1, steps
for n in [7, 19, 4, 100, 2]:
    h, s = path(n)
    print(f"{n}: {'happy' if h else 'unhappy'} after {len(s) - 1} steps: " + " > ".join(str(x) for x in s[:6]))
hs = [n for n in range(1, 51) if path(n)[0]]
print("happy up to 50: " + " ".join(map(str, hs)))
print(f"count: {len(hs)}")

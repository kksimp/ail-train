def nv(n): return sum(int(d) ** 2 for d in str(n))
def ch(n):
    s = []; x = n
    while x != 1 and x not in s: s.append(x); x = nv(x)
    s.append(x); return s
print("happy: " + " ".join(str(n) for n in range(1, 51) if ch(n)[-1] == 1))
for n in [7, 4, 19]: print(f"{n}: " + " -> ".join(map(str, ch(n))))

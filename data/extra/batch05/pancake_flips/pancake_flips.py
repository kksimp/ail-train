def fl(x, k): return x[:k][::-1] + x[k:]
s = [3, 6, 1, 8, 4, 2, 7, 5]; f = 0; n = len(s)
while n > 1:
    b = max(range(n), key=lambda i: (s[i], -i))
    if b != n - 1:
        if b > 0: s = fl(s, b + 1); f += 1; print(f"flip {b + 1}: [{', '.join(map(str, s))}]")
        s = fl(s, n); f += 1; print(f"flip {n}: [{', '.join(map(str, s))}]")
    n -= 1
print(f"{f} flips")

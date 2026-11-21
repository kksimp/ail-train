def recover(xs, ys, p):
    total = 0
    for i in range(len(xs)):
        num = 1
        den = 1
        for j in range(len(xs)):
            if j != i:
                num = num * (p - xs[j]) % p
                den = den * ((xs[i] - xs[j] + p) % p) % p
        term = ys[i] * num % p * pow(den, p - 2, p) % p
        total = (total + term) % p
    return total
p = 7919
coef = [1234, 166, 94]
shares = []
for x in range(1, 6):
    y = (coef[0] + coef[1] * x + coef[2] * x * x) % p
    shares.append(y)
    print(f"holder {x} gets ({x}, {y})")
for pick in [[1, 2, 3], [2, 4, 5], [1, 3, 5]]:
    ys = [shares[x - 1] for x in pick]
    print(f"holders [{', '.join(map(str, pick))}] rebuild {recover(pick, ys, p)}")
print(f"holders [1, 2] alone get {recover([1, 2], [shares[0], shares[1]], p)}")

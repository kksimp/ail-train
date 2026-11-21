def best_line(xs):
    take = 0
    skip = 0
    for x in xs:
        t = skip + x
        skip = max(skip, take)
        take = t
    return max(take, skip)

def chosen(xs):
    n = len(xs)
    dp = [0, xs[0]]
    for i in range(1, n):
        dp.append(max(dp[i], dp[i - 1] + xs[i]))
    out = []
    i = n
    while i > 0:
        if dp[i] == dp[i - 1]:
            i -= 1
        else:
            out.append(i)
            i -= 2
    return out[::-1]

street = [12, 7, 9, 30, 2, 14, 20, 5, 8, 16]
print(f"pledges: {street}")
print(f"best on the street: {best_line(street)}")
print(f"houses called at: {chosen(street)}")
close = [20, 4, 6, 18, 9, 22]
a = best_line(close[0:len(close) - 1])
b = best_line(close[1:])
print(f"ring close {close}: skip last {a}, skip first {b}, best {max(a, b)}")

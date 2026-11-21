def pell(d):
    a0 = 0
    while (a0 + 1) * (a0 + 1) <= d:
        a0 += 1
    m, den, a = 0, 1, a0
    h_prev, h, k_prev, k = 1, a0, 0, 1
    terms = 1
    while h * h - d * k * k != 1:
        m = den * a - m
        den = (d - m * m) // den
        a = (a0 + m) // den
        h_new = a * h + h_prev
        k_new = a * k + k_prev
        h_prev, h = h, h_new
        k_prev, k = k, k_new
        terms += 1
    return [h, k, terms]

for d in [2, 3, 5, 7, 13, 19, 29]:
    x, y, t = pell(d)
    x2 = x * x + d * y * y
    y2 = 2 * x * y
    print(f"D = {d:>2}: x = {x:>5}, y = {y:>4} after {t} convergents; next {x2}, {y2}")

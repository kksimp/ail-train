def eas(y):
    a = y % 19; b, c = divmod(y, 100); d, e = divmod(b, 4); f = (b + 8) // 25; g = (b - f + 1) // 3
    h = (19 * a + b - d - g + 15) % 30; i, k = divmod(c, 4); l = (32 + 2 * e + 2 * i - h - k) % 7
    m = (a + 11 * h + 22 * l) // 451; n = h + l - 7 * m + 114
    return n // 31, n % 31 + 1
sh = lambda md: f"{md[1]} {'March' if md[0] == 3 else 'April'}"
for y in [2024, 2025, 2026, 2027, 2028, 2038]: print(f"{y}: {sh(eas(y))}")
ys = range(2000, 2100)
e = min(ys, key=lambda y: eas(y)[0] * 100 + eas(y)[1]); l = max(ys, key=lambda y: eas(y)[0] * 100 + eas(y)[1])
print(f"earliest 2000-2099: {e} ({sh(eas(e))})")
print(f"latest 2000-2099: {l} ({sh(eas(l))})")

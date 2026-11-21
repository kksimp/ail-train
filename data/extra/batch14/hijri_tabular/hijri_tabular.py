def jdn(y, m, d):
    a = (14 - m) // 12
    yy = y + 4800 - a
    mm = m + 12 * a - 3
    return d + (153 * mm + 2) // 5 + 365 * yy + yy // 4 - yy // 100 + yy // 400 - 32045
def hijri(jd):
    l = jd - 1948440 + 10632
    n = (l - 1) // 10631
    l = l - 10631 * n + 354
    j = ((10985 - l) // 5316) * ((50 * l) // 17719) + (l // 5670) * ((43 * l) // 15238)
    l = l - ((30 - j) // 15) * ((17719 * j) // 50) - (j // 16) * ((15238 * j) // 43) + 29
    m = (24 * l) // 709
    d = l - (709 * m) // 24
    return [30 * n + j - 30, m, d]
def is_leap(y):
    return (14 + 11 * y) % 30 < 11
months = ["Muharram", "Safar", "Rabi I", "Rabi II", "Jumada I", "Jumada II", "Rajab", "Shaban", "Ramadan", "Shawwal", "Dhu al-Qada", "Dhu al-Hijja"]
for y, m, d in [[622, 7, 19], [2000, 1, 1], [2024, 3, 11], [2026, 11, 21], [2030, 1, 5]]:
    h = hijri(jdn(y, m, d))
    print(f"{y}-{m:02}-{d:02} is {h[2]} {months[h[1] - 1]} {h[0]} AH")
leaps = [y for y in range(1441, 1471) if is_leap(y)]
print(f"leap years in the cycle 1441-1470: [{', '.join(map(str, leaps))}]")
days = sum(355 if is_leap(y) else 354 for y in range(1441, 1471))
print(f"30 lunar years = {days} days, mean month {days / 360.0:.5f} days")

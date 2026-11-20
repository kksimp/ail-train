def hd(h, m):
    d = abs((h % 12) * 60 + m - m * 12)
    return min(d, 720 - d)
def show(x):
    return f"{x // 2}" if x % 2 == 0 else f"{x // 2}.5"
for t in ["3:00", "12:30", "9:45", "6:00", "2:20", "11:59", "0:00"]:
    h, m = map(int, t.split(":"))
    print(f"{t:>5} {show(hd(h, m)):>6} degrees")
print(f"hours with an overlap within 1 degree: {sum(1 for h in range(12) if hd(h, (h * 60) // 11) <= 2)}")

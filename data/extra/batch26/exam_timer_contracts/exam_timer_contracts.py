start = 9 * 60 + 30
c = lambda m: f"{m // 60:02}:{m % 60:02}"
last = start
for i, base, pct in [("A101", 120, 0), ("A102", 120, 25), ("A103", 90, 50), ("A104", 150, 10), ("A105", 90, 100)]:
    mins = base + base * pct // 100
    rests = mins // 60
    ends = start + mins + rests * 10
    last = max(last, ends)
    print(f"{i}: {base} min +{pct}% = {mins} min, {rests} breaks, ends {c(ends)}")
print(f"invigilators stay until {c(last)}")

import math

def split_secs(s):
    parts = s.split(":")
    return int(parts[0]) * 60.0 + float(parts[1])

def show(t):
    tenths = int(math.floor(t * 10.0 + 0.5))
    m = tenths // 600
    s = tenths % 600
    sec = str(s // 10).rjust(2, '0')
    return f"{m}:{sec}.{s % 10}"

def watts(split):
    pace = split / 500.0
    return 2.8 / (pace * pace * pace)

for s in ["2:30.0", "2:00.0", "1:52.5", "1:45.0", "1:38.2", "1:30.0"]:
    t = split_secs(s)
    print(f"split {s}  {watts(t):>6.1f} W  2k in {show(t * 4.0)}")
for w in [100.0, 200.0, 300.0, 400.0]:
    pace = math.cbrt(2.8 / w)
    print(f"{w:.0f} W needs a split of {show(pace * 500.0)}")

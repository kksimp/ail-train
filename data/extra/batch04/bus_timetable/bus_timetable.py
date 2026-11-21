def hm(m): return f"{m // 60:02}:{m % 60:02}"
def tm(s): h, m = s.split(":"); return int(h) * 60 + int(m)
B = list(range(tm("06:30"), tm("09:00") + 1, 12)); print(f"{len(B)} buses, last at {hm(B[-1])}")
for a in ["06:10", "06:42", "07:15", "08:59", "09:05"]:
    n = [b for b in B if b >= tm(a)]
    print(f"{a}: no more buses" if not n else f"{a}: bus at {hm(n[0])}, wait {n[0] - tm(a)} min")

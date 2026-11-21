def pl(n, u): return f"1 {u} ago" if n == 1 else f"{n} {u}s ago"
def ag(s):
    if s < 45: return "just now"
    if s < 3600: return pl((s + 30) // 60, "minute")
    if s < 86400: return pl(s // 3600, "hour")
    d = s // 86400
    if d == 1: return "yesterday"
    if d < 14: return f"{d} days ago"
    if d < 60: return pl(d // 7, "week")
    if d < 365: return pl(d // 30, "month")
    return pl(d // 365, "year")
for s in [10, 50, 125, 3599, 3600, 7300, 86399, 90000, 400000, 1500000, 4000000, 40000000, 80000000]: print(f"{s:>8} s: {ag(s)}")

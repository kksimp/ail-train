class Quota:
    def __init__(s, soft, hard, used):
        s.soft, s.hard, s.used, s.grace_from = soft, hard, used, -1
    def write(s, day, mb):
        after = s.used + mb
        if mb > 0 and after > s.hard:
            return f"refused, would pass hard limit {s.hard}"
        if mb > 0 and after > s.soft:
            if s.grace_from < 0:
                s.grace_from = day
            elif day - s.grace_from >= 7:
                return f"refused, grace ran out on day {s.grace_from + 7}"
        s.used = after
        if s.used <= s.soft:
            s.grace_from = -1
            return "ok"
        left = 7 - (day - s.grace_from)
        return f"ok, over soft limit, {left} grace days left"

q = Quota(100, 120, 80)
events = [(1, 15), (2, 10), (3, 20), (4, 5), (6, 3), (9, 2), (10, -30), (11, 25), (12, 10), (19, 2)]
for day, mb in events:
    msg = q.write(day, mb)
    print(f"day {day:>2} {mb:>4} MB -> used {q.used:>3}: {msg}")

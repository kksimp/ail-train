def days(s): return s[1] // (s[2] * s[3])
def refill_day(s): return s[4] + (days(s) * 8 + 9) // 10
scripts = [("metformin 500", 112, 2, 2, 3), ("amlodipine 5", 30, 1, 1, 10), ("prednisolone 5", 60, 4, 1, 20), ("atorvastatin 20", 90, 1, 1, 1)]
for s in scripts:
    print(f"{s[0]:<16} {s[1]:>3} tablets = {days(s):>2} days, refill from day {refill_day(s)}")
for drug, day in [("metformin 500", 27), ("amlodipine 5", 33), ("prednisolone 5", 31), ("atorvastatin 20", 75)]:
    s = [x for x in scripts if x[0] == drug][0]
    verdict = "fill" if day >= refill_day(s) else f"too early, wait {refill_day(s) - day} days"
    print(f"day {day:>2} request for {drug}: {verdict}")

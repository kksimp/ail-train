import datetime
today = datetime.date(2026, 11, 20)
for name, born in [("Ade", "1990-05-17"), ("Bea", "2000-02-29"), ("Cas", "2026-01-01"), ("Dov", "1969-07-20")]:
    age = (today - datetime.date.fromisoformat(born)).days
    nxt = (age // 1000 + 1) * 1000
    print(f"{name}: {age:,} days old, {nxt:,} days in {nxt - age} days")
print(0)

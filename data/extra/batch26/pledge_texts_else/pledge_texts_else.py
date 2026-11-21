texts = ["PLEDGE 20", "PLEDGE 5", "pledge ten", "PLEDGE 50", "STOP", "PLEDGE -5", "PLEDGE 1O", "PLEDGE 15"]
total = 0; n = 0
for t in texts:
    if not t.startswith("PLEDGE "):
        print(f"ignored '{t}'"); continue
    a = t[len("PLEDGE "):]
    if a.startswith("-"):
        print(f"refused negative pledge {a}"); continue
    if not a.isdigit():
        print(f"unreadable amount '{a}'"); continue
    total += int(a); n += 1
    print(f"pledge of {a}, running total {total}")
print(f"{n} pledges, {total} pounds, {len(texts) - n} texts not counted")

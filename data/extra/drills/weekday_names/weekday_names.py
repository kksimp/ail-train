DAYS = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

def parse_day(text):
    t = text.strip()
    if len(t) < 3:
        return None
    fixed = t[:1].upper() + t[1:3].lower()
    return fixed if fixed in DAYS else None

for i, d in enumerate(DAYS):
    kind = "weekend" if d in ("Sat", "Sun") else "workday"
    print(f"{d} {kind} -> {DAYS[(i + 1) % 7]}")
print(7)
for text in ["fri", " SUNDAY ", "Mon", "xx", "noday"]:
    d = parse_day(text)
    if d:
        print(f"{text.strip()} is {d}")
    else:
        print(f"{text.strip()} is not a day")
print("true")
print("true")

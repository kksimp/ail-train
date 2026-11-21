def queue_minutes(t):
    h = t // 60
    if 5 <= h <= 7:
        return 35
    if 8 <= h <= 10:
        return 25
    if 16 <= h <= 18:
        return 30
    return 15

def rush(t):
    h = t // 60
    return (7 <= h < 9) or (16 <= h < 18)

def hhmm(t):
    return f"{t // 60:02d}:{t % 60:02d}"

def leave_by(dep, intl):
    close = 90 if intl else 60
    at_desk = dep - close
    at_airport = at_desk - queue_minutes(at_desk)
    calm = at_airport - 45
    return at_airport - 70 if rush(calm) or rush(at_airport - 70) else calm

flights = [(410, False, "Belfast"), (555, True, "Lisbon"), (630, False, "Jersey"), (1050, False, "Inverness"), (1145, True, "Oslo")]
earliest = 24 * 60
for dep, intl, city in flights:
    leave = leave_by(dep, intl)
    close = 90 if intl else 60
    q = queue_minutes(dep - close)
    drive = dep - close - q - leave
    earliest = min(earliest, leave)
    print(f"{city:<9} {hhmm(dep)}: leave home {hhmm(leave)} (drive {drive}, queue {q})")
print(f"earliest start of the week: {hhmm(earliest)}")

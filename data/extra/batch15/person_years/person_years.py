cohort = [("shift", 0, 60, False), ("shift", 0, 23, True), ("shift", 6, 60, False), ("shift", 12, 41, True), ("shift", 0, 17, False), ("shift", 3, 52, True), ("day", 0, 60, False), ("day", 0, 60, False), ("day", 9, 48, True), ("day", 0, 60, False), ("day", 2, 35, False), ("day", 0, 60, False), ("day", 14, 60, False)]
months = {}; events = {}
for g, s, e, ev in cohort:
    months[g] = months.get(g, 0) + e - s
    if ev: events[g] = events.get(g, 0) + 1
rates = {}
for g, mo in months.items():
    years = float(mo) / 12.0
    e = events.get(g, 0)
    rate = float(e) / years * 1000.0
    rates[g] = rate
    print(f"{g:<5} {e} events in {years:.2f} person-years: {rate:.1f} per 1000 person-years")
print(f"rate ratio shift / day: {rates['shift'] / rates['day']:.2f}")

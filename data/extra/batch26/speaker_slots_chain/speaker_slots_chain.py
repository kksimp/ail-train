conf = ["Okafor", "Lindqvist", "Ruiz"]; wait = ["Chen", "Haddad", "Novak"]
times = ["09:00", "09:40", "10:20", "11:00", "11:40"]
plan = list(zip(times, conf + wait))
for t, w in plan:
    print(f"{t} {w}{'' if w in conf else ' (from waitlist)'}")
print(f"{len(plan)} slots filled, {len(wait) - (len(plan) - len(conf))} still waiting")
rb = [w for i, w in enumerate(conf + wait) if i % 2 == 1]
print(f"if every second talk moved to room B: {', '.join(rb)}")

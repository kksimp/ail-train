limits = {"Urgent": 2, "High": 8, "Normal": 24}
tiers = ["Desk", "Specialist", "Manager"]
tickets = [[101, "Urgent", 0, 0, False], [102, "High", 1, 0, False], [103, "Normal", 2, 0, False], [104, "Urgent", 5, 0, False], [105, "High", 6, 0, False]]
closes = {104: 6, 102: 12}
for now in [4, 8, 12, 16, 30]:
    for t in tickets:
        if closes.get(t[0], 1000) <= now and not t[4]:
            t[4] = True
            print(f"hour {now:>2}: #{t[0]} closed at Tier.{tiers[t[3]]}")
        if not t[4] and now >= t[2]:
            waited = now - t[2]
            steps = waited // limits[t[1]]
            target = min(steps, 2)
            if target != t[3]:
                t[3] = target
                note = ", page the manager" if target == 2 else ""
                print(f"hour {now:>2}: #{t[0]} Priority.{t[1]} waited {waited}h -> Tier.{tiers[target]}{note}")
open_ids = [t[0] for t in tickets if not t[4]]
print(f"open at the end: {open_ids}")

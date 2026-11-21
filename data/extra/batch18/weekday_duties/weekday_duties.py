people = ["Asha", "Bruno", "Chen"]
days = ["Mon", "Tue", "Wed", "Thu", "Fri"]
rota = {d: people[i % 3] for i, d in enumerate(days)}
for d in days: print(f"{d}: {rota[d]}")
for who, t in [("Bruno", "Thu"), ("Chen", "Sat"), ("Asha", "Tue")]:
    if t in rota:
        old = rota[t]; rota[t] = who; print(f"{who} takes Day.{t} from {old}")
    else: print(f"{who}: no duty on {t}")
print(f"duties per person: {[sum(1 for x in rota.values() if x == p) for p in people]}")

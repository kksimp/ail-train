doses = ["6-in-1 first", "6-in-1 second", "6-in-1 third", "MMR"]
weeks = [8, 12, 16, 52]
now = 70
children = [("Ava", 10, [0, 1, 2]), ("Ben", 50, [0]), ("Cal", 0, [0, 1, 2, 3]), ("Dee", 64, []), ("Eli", 5, [0, 2])]
chase = 0
for name, born, given in children:
    late = [i for i in range(len(weeks)) if i not in given and born + weeks[i] < now]
    chase += len(late)
    late_text = "none overdue" if not late else "overdue: " + ", ".join(doses[i] for i in late)
    upcoming = [i for i in range(len(weeks)) if i not in given and born + weeks[i] >= now]
    next_text = "nothing more due" if not upcoming else f"next {doses[upcoming[0]]} in week {born + weeks[upcoming[0]]}"
    print(f"{name}: age {now - born} weeks, {late_text}; {next_text}")
print(f"{chase} doses to chase")

def decide(breach, run, hold):
    if not breach:
        return "Ok"
    if run >= hold:
        return "Firing"
    return "Pending"

samples = [55, 82, 85, 79, 83, 88, 91, 95, 70, 65, 81, 84, 86, 87, 60]
limit = 80
hold = 3
state = "Ok"
run = 0
firing_minutes = 0
episodes = 0
for i, v in enumerate(samples):
    breach = v > limit
    run = run + 1 if breach else 0
    nxt = decide(breach, run, hold)
    if nxt != state:
        print(f"t={i:>2} cpu {v:>3}: {state} -> {nxt}")
        if nxt == "Firing":
            episodes += 1
        state = nxt
    if state == "Firing":
        firing_minutes += 1
print(f"fired {episodes} times, {firing_minutes} minutes in total")

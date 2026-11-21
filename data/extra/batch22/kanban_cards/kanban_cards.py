def cards(daily, lead, safety, container):
    need = daily * lead * (100 + safety)
    per = container * 100
    return (need + per - 1) // per

parts = [("bracket", 400, 2, 50, 10), ("hinge", 120, 3, 40, 20), ("panel", 60, 5, 12, 15), ("screw pack", 900, 1, 250, 25)]
total = 0
for name, daily, lead, container, safety in parts:
    n = cards(daily, lead, safety, container)
    total += n
    cover = n * container * 10 // daily
    print(f"{name:<10} {n:>2} cards of {container:>3}: at most {n * container} on hand, {cover // 10}.{cover % 10} days of use")
print(f"{total} cards in the loop")
